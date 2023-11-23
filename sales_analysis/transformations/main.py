import os
import sys
from sqlalchemy import text
import logging
from dotenv import load_dotenv
import shutil
from datetime import datetime
from pyspark.sql.functions import expr
from pyspark.sql.functions import concat_ws,lit


load_dotenv()
sys.path.append(os.getcwd())

from sales_analysis.spark_utils.session_provider import get_mysql_session
from sales_analysis.spark_utils.session_provider import get_spark_session
from sales_analysis.s3_utils.s3_client_provider import S3ClientProvider
from sales_analysis.s3_utils.s3_client_util import S3Util
from sales_analysis.spark_utils.spark_util import SparkUtil
from resources import env_config
from queries import *
from sales_analysis.common_utils.local_operations import delete_local_file
from resources.constants import ms_url,properties,fact_data_schema
from customer_mart_transform import customer_mart_calculation_table_write
from sales_mart_transform import sales_mart_calculation_write
from sales_analysis.common_utils.logger import logger
logger()

spark = get_spark_session()
s3_client = S3ClientProvider().get_client()
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def checkpointing():
    #to check what happened with the last run.
    csv_files = [file for file in os.listdir(env_config.get("local_dir")) if file.endswith(".csv")]
    # print(csv_files)
    engine = get_mysql_session()
    if csv_files:
        with engine.connect() as conn:
            op_obj= conn.execute(text(get_failed_files.format(db=env_config.get("ms_db"),p_stg_table=env_config.get("p_stg_tbl"),
                                                    file_names=str(csv_files)[1:-1])))
            data = op_obj.fetchall()
            if data:
                logging.info("Last run was failed.")
            else:
                logging.info("No record match")
    else:
        logging.info("last run was successful..")

def get_files_from_s3():
    try:
        folder_path = env_config.get("s3_source_dir")
        files = S3Util.list_files(s3_client=s3_client,bucket=env_config.get("bucket"),file_path=folder_path)
        logging.info(f"Available files in s3 bucket {files}")
        if not files:
            logging.error(f"No files available @{folder_path}")
    except Exception as e:
        logging.exception(e)        

    S3Util.download_files(s3_client,env_config.get("bucket"),files,os.path.join(os.getcwd(),env_config.get("local_s3_dir")))

    all_files = os.listdir(os.path.join(os.getcwd(),env_config.get("local_s3_dir")))
    logging.info(f"Files available {all_files}")

    if all_files:
        csv_files = []
        other_files = []
        for file in all_files:
            if file.endswith('.csv'):
                csv_files.append(os.path.abspath(os.path.join(env_config.get("local_s3_dir"),file)))
            else:
                other_files.append(os.path.abspath(os.path.join(env_config.get("local_s3_dir"),file)))
        if not csv_files:
            logging.error("No csv files available to process")
    else:
        logging.exception("No data to process.")
        
    logging.info(f"Files needs to be processed are {csv_files}")
    return csv_files

def schema_validation(files):

    correct_files = []
    error_files =[]
    for data in files:
        data_schema = spark.read.format("csv")\
                        .option("header","true")\
                        .load(data).columns
        logging.info(f"{data} schema is {data_schema}")
        mandatory_cols = env_config.get('mandatory_cols').split(',')
        logging.info(f"Mandatory columns is {mandatory_cols}")
        missing_cols = set(mandatory_cols)-set(data_schema)
        logging.info(f"Missing cols are {missing_cols}")
        
        if missing_cols:
            error_files.append(data)
        else:
            logging.info(f"No missing cols for {data}")
            correct_files.append(data)
            
    logging.info(f"correct files {correct_files}")
    logging.info(f"error files {error_files}")

    error_folder_local = env_config.get("local_err_dir")
    if error_files:
        for file in error_files:
            if os.path.exists(file):
                file_name = os.path.basename(file)
                destination_path = os.path.join(error_folder_local,file_name)
                
                shutil.move(file,destination_path)
                logging.info(f"Moved {file} into {destination_path}")
                
                source_prefix = env_config.get("s3_source_dir")
                dest_prefix = env_config.get("s3_err_dir")
                
                S3Util.move_files(s3_client,env_config.get("bucket"),source_prefix,dest_prefix,file)
            else:
                logging.error(f"{file} doesn't exist.")

    else:
        logging.info("Hurray !! No error files at the moment....")
    return correct_files
    
def update_tbl(correct_files):
    logging.info("started processing the data")
    #status -> A(active) , I(inactive)
    #It'll remain A if failed in between due to some exception

    insert_statements = []
    if correct_files:
        for file in correct_files:
            file_name = os.path.basename(file)
            statements = insert_process_query.format(db=env_config.get("ms_db"),p_stg_table=env_config.get("p_stg_tbl"),filename=file_name,current_dt=current_date)
            insert_statements.append(statements)
        logging.info("created statements.")
        engine = get_mysql_session()
        with engine.connect() as conn:
            for statement in insert_statements:
                conn.execute(text(statement))
                conn.commit()
    else:
        logging.info("No files to process")
        raise Exception("No data available to process at the moment..")

def get_data(correct_files):
    
    df = spark.createDataFrame([],schema=fact_data_schema)
    logging.info("**  Created a empty df with fact data schema **")
    df.show()


    mandatory_cols = env_config.get('mandatory_cols').split(',')
    for data in correct_files:
        data_df = spark.read.format("csv")\
                .option("header","true")\
                .option("inferSchema","true")\
                .load(data)
        data_schema = data_df.columns
        extra_cols = list(set(data_schema)-set(mandatory_cols))
        logging.info(f"Extra cols are {extra_cols}")
        if extra_cols:
            data_df = data_df.withColumn("additional_column",concat_ws(", ",*extra_cols))\
                    .select(*mandatory_cols,"additional_column")
            logging.info("Processed data and added 'additional_column'")
        else:
            data_df = data_df.withColumn("additional_column",lit(None))\
                    .select(*mandatory_cols,"additional_column")
                    #.select("customer_id","store_id","product_name","sales_date","sales_person_id",
                    #        "price","quantity","total_cost","additional_column")
        df = df.union(data_df)

    df.show()


    logging.info("**** Loading customer data *****")
    customer_table_df = SparkUtil.get_db_data(spark,env_config.get("customer_table_name"),ms_url,properties)

    # logging.info("**** Loading product data *****")
    # product_table_df = SparkUtil.get_db_data(spark,env_config.get("product_table_name"),ms_url,properties)

    # logging.info("**** Loading product staging data *****")
    # product_staging_table_df = SparkUtil.get_db_data(spark,env_config.get("p_stg_tbl"),ms_url,properties)

    logging.info("**** Loading sales team data *****")
    sales_team_table_df = SparkUtil.get_db_data(spark,env_config.get("sales_team_table"),ms_url,properties)


    logging.info("**** Loading store data *****")
    store_table_df = SparkUtil.get_db_data(spark,env_config.get("store_table"),ms_url,properties)


    s3_customer_store_sales_df_join = SparkUtil.dimensions_table_join(df,
                                                            customer_table_df,
                                                            store_table_df,
                                                            sales_team_table_df)
    return s3_customer_store_sales_df_join



checkpointing()
files = get_files_from_s3()
correct_files = schema_validation(files)
update_tbl(correct_files)
s3_customer_store_sales_df_join = get_data(correct_files)
logging.info("************** Final enriched data ********************")
s3_customer_store_sales_df_join.show(30)
s3_customer_store_sales_df_join.printSchema()

#customer data into customer data mart in parquet
#file in local first then to s3
#this is used for reporting,data science

logging.info("Writing data into customer data mart")
final_customer_data_mart_df = s3_customer_store_sales_df_join\
                              .select("ct.customer_id","ct.first_name","ct.last_name",
                                      "ct.address","ct.pincode","phone_number","sales_date","total_cost")
                              #last 2 columns are from fact[main] table
final_customer_data_mart_df.show()

SparkUtil.writer(final_customer_data_mart_df,'overwrite','parquet',env_config.get("local_customer_data_mart_dir"))

logging.info(f"written customer data mart to local...{env_config.get('local_customer_data_mart_dir')}")

S3Util.upload_files(s3_client,env_config.get("bucket"),env_config.get("local_customer_data_mart_dir"),env_config.get("s3_customer_datamart_dir"),True)


logging.info("Writing data into sales team data mart")
final_sales_team_data_mart_df = s3_customer_store_sales_df_join\
                            .select("store_id","sales_person_id","sales_person_first_name","sales_person_last_name",
                                    "store_manager_name","manager_id","is_manager","sales_person_address","sales_person_pincode",
                                    "sales_date","total_cost",expr("SUBSTRING(sales_date,1,7) as sales_month"))
                            #sales month is to provide incentives..               
final_sales_team_data_mart_df.show()
SparkUtil.writer(final_sales_team_data_mart_df,'overwrite','parquet',env_config.get("local_sales_team_data_mart_dir"))
logging.info(f" sales team data written to local disk {env_config.get('local_sales_team_data_mart_dir')}")

S3Util.upload_files(s3_client,env_config.get("bucket"),env_config.get("local_sales_team_data_mart_dir"),env_config.get("s3_sales_datamart_dir"),True)
logging.info("uploaded to s3")



logging.info("*************** Partitions ***************")
             
final_sales_team_data_mart_df.write.format("parquet")\
    .option("header","true")\
    .mode("overwrite")\
    .partitionBy("sales_month","store_id")\
    .option("path",env_config.get("local_sales_team_data_mart_part_partitioned_dir"))\
    .save()             
             
s3_prefix = env_config.get("s3_sales_partitioned_dir")
current_epoch = int(datetime.now().timestamp()) * 1000
for root,dir,files in os.walk(env_config.get("local_sales_team_data_mart_part_partitioned_dir")):
    for file in files:
        print(file)
        local_file_path = os.path.join(root,file)
        relative_file_path = os.path.relpath(local_file_path,env_config.get("local_sales_team_data_mart_part_partitioned_dir"))
        s3_key = f"{s3_prefix}/{current_epoch}/{relative_file_path}"
        s3_client.upload_file(local_file_path,env_config.get('bucket'),s3_key)


#calc for customer mart
#find out customer total purchases every month (write into table) 
logging.info("***** Calculatig customer every month purchased amount **********")
customer_mart_calculation_table_write(final_customer_data_mart_df)
logging.info("********** Calc of customer mart done and written into table ***********")

logging.info("*******  Calc sales every month **********")
sales_mart_calculation_write(final_sales_team_data_mart_df)
logging.info("********** Calc of sales mart done and written into table ***********")

source_prefix = env_config.get("s3_source_dir")
destination_prefix = env_config.get("s3_processed_dir")
S3Util.move_files(s3_client,env_config.get('bucket'),source_prefix,destination_prefix)
logging.info("Processing is done")


#Clean local directories.
logging.info("*** Deleting sales data")
delete_local_file(env_config.get("local_s3_dir"))

logging.info("Deleting customer mart data")
delete_local_file(env_config.get("local_customer_data_mart_dir"))

logging.info("deleting sales team data mart")
delete_local_file(env_config.get("local_sales_team_data_mart_dir"))

logging.info("deletig sales partitioned")
delete_local_file(env_config.get("local_sales_team_data_mart_part_partitioned_dir"))

logging.info("Done, deleted data from local...")

#update status to inactive...
update_statements = []
if correct_files:
    for file in correct_files:
        filename = os.path.basename(file)
        update_statements.append(update_process_query.format(db=env_config.get("ms_db"),p_stg_table=env_config.get("p_stg_tbl"),filename=filename,current_dt=current_date))
    logging.info("Update statements created.")
    engine = get_mysql_session()
    with engine.connect() as conn:
        for statement in update_statements:
            conn.execute(text(statement))
            conn.commit()
    logging.info("table has been updated.")
else:
    logging.error("No correct files, must be some error. Pls check")

input("type something to terminate the session.") #mean while you can check sparkUI @<sparkhost>:4040/jobs
