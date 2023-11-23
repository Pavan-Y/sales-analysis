import logging
from pyspark.sql.functions import col

class SparkUtil:
    
    def get_db_data(spark,table_name,url,prop):
        df = spark.read.jdbc(url=url,
                             table=table_name,
                             properties=prop)
        return df

    def dimensions_table_join(final_df,customer_df,store_df,sales_team_df):
        logging.info("Joining final df with customer df")
        s3_customer_df_join = final_df.alias("s3_data")\
                            .join(customer_df.alias("ct"),
                                  col("s3_data.customer_id") == col("ct.customer_id"),"inner")\
                            .drop("product_name","price","quantity","additional_column","s3_data.customer_id","customer_joining_date")    
        
        s3_customer_df_join.printSchema()
        
        logging.info("Joining s3 customer df with store table df")
        s3_customer_store_df_join = s3_customer_df_join.join(store_df,store_df["id"]==s3_customer_df_join["store_id"],"inner")\
                                    .drop("id","store_pincode","store_opening_date","reviews")
        
        logging.info("Joining s3 customer store df with sales team df")
        s3_customer_store_sales_df_join = s3_customer_store_df_join.join(sales_team_df.alias("st"),
                                                        col("st.id")==s3_customer_store_df_join["sales_person_id"],"inner")\
                                         .withColumn("sales_person_first_name",col("st.first_name"))\
                                         .withColumn("sales_person_last_name",col("st.last_name"))\
                                         .withColumn("sales_person_address",col("st.address"))\
                                         .withColumn("sales_person_pincode",col("st.pincode"))\
                                         .drop("id","st.first_name","st.last_name","st.address","st.pincode")
                                         
        return s3_customer_store_sales_df_join
    
    def writer(df,mode,format,file_path):
        try:
            df.write.format(format)\
                .option("header","true")\
                .mode(mode)\
                .option("path",file_path)\
                .save()
        except Exception as e:
            logging.exception(e)
            raise e
        
    def write_df(df,table,url,props):
        try:
            df.write.jdbc(url=url,
                        table=table,
                        mode="append",
                        properties=props)
            logging.info(f"Successfully written into {table}")
        except Exception as e:
            logging.exception(e)
            raise e