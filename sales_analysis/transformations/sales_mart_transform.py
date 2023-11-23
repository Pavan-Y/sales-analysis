from pyspark.sql.functions import *
from pyspark.sql.window import Window
from resources import env_config
from resources.constants import ms_url,properties
from sales_analysis.spark_utils.spark_util import SparkUtil
import logging

def sales_mart_calculation_write(final_sales_mart_df):
    window = Window.partitionBy("store_id","sales_person_id","sales_month")
    final_sales_team_data_mart = final_sales_mart_df.withColumn("sales_month",substring(col("sales_date"),1,7))\
                                 .withColumn("total_sales_every_month",sum(col("total_cost")).over(window))\
                                 .select("store_id","sales_person_id",concat(col("sales_person_first_name"),lit(' '),
                                                                        col("sales_person_last_name")).alias("full_name"),
                                         "sales_month","total_sales_every_month").distinct()
    rank_window = Window.partitionBy("store_id","sales_month")\
                    .orderBy(col("total_sales_every_month").desc())
    final_sales_team_data_mart_table = final_sales_team_data_mart\
                                    .withColumn("rnk",rank().over(rank_window))\
                                    .withColumn("incentive",when(col("rnk")==1, col("total_sales_every_month")*0.01).otherwise(lit(0)))\
                                    .withColumn("incentive",round(col("incentive"),2))\
                                    .withColumn("total_sales",col("total_sales_every_month"))\
                                    .select("store_id","sales_person_id","full_name","sales_month","total_sales","incentive")
                                    
    logging.info("*** writting to tbl***")
    SparkUtil.write_df(final_sales_team_data_mart_table,env_config.get("sales_team_data_mart_table"),ms_url,properties)