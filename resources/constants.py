from pyspark.sql.types import StructField,StructType,StringType,BooleanType,IntegerType,FloatType,DateType,DecimalType
from resources import env_config

fact_data_schema = StructType([
                   StructField("customer_id",IntegerType(),True),
                   StructField("store_id",IntegerType(),True),
                   StructField("product_name",StringType(),True),
                   StructField("sales_date",DateType(),True),
                   StructField("sales_person_id",IntegerType(),True),
                   StructField("price",FloatType(),True),
                   StructField("quantity",FloatType(),True),
                   StructField("total_cost",FloatType(),True),
                   StructField("additional_column",StringType(),True)
])

customer_schema = StructType([
    StructField("customer_id", IntegerType(), True),
    StructField("full_name", StringType(), True),
    StructField("address", StringType(), True),
    StructField("phone_number", StringType(), True),
    StructField("sales_date_month", StringType(), True),
    StructField("total_sales", DecimalType(10, 2), True)
])

sales_team_schema = StructType([
    StructField("store_id", IntegerType(), True),
    StructField("sales_person_id", IntegerType(), True),
    StructField("full_name", StringType(), True),
    StructField("sales_month", StringType(), True),
    StructField("total_sales", DecimalType(10, 2), True),
    StructField("incentive", DecimalType(10, 2), True)
])

ms_url = f"jdbc:mysql://{env_config.get('ms_host')}:{env_config.get('ms_port')}/{env_config.get('ms_db')}"
properties = {"user":env_config.get("ms_user"),"password":env_config.get("ms_pass"),"driver":"com.mysql.cj.jdbc.Driver"}