from sqlalchemy import create_engine
import findspark
from pyspark.sql import SparkSession
import logging

from resources import env_config

def get_mysql_session():
    user,password,host,port,database=env_config.get("ms_user"),env_config.get("ms_pass"),env_config.get("ms_host"),env_config.get("ms_port"),env_config.get("ms_db")
    connection_url = f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}' #pip install mysql-connector-python
    engine = create_engine(connection_url)
    return engine


def get_spark_session():
    logging.info("******************** Starting the Spark session *********************")
    findspark.init()
    spark = SparkSession.builder.master("local[*]")\
            .appName("sales_analysis")\
            .getOrCreate()
    logging.info("***************** Spark session is ready now **********************")
    return spark