import uuid
from datetime import datetime,timedelta
import os
import pandas as pd
import random
import logging
import sys,os
sys.path.append(os.getcwd())

from resources import env_config
from sales_analysis.s3_utils.s3_client_provider import S3ClientProvider
from sales_analysis.s3_utils.s3_client_util import S3Util

#50 customers
customer_ids = [i for i in range(1,51)]

#15 stores
store_ids = [i for i in range(901, 916)]

product_data = {"apple":100, "banana":20, "orange":30, "bread":50, "milk":150, 
    "cheese":300, "lettuce":80, "chicken":250, "rice":100, "tomato":45}


sales_persons = {store_id: [j for j in range((i - 1) * 3 + 1, i * 3 + 1)] for i, store_id in enumerate(store_ids, start=1)}


files_path = env_config.get("local_dir")

input_date_str = input("Enter the date for which you want to generate (YYYY-MM-DD): ")
input_date = datetime.strptime(input_date_str, "%Y-%m-%d")
sales_data_file = os.path.join(files_path,f"sales_data_{input_date_str}.csv")
#print(sales_data_file)
# with open(sales_data_file,'w',newline="") as csvfile:
#     writer = csv.
reqd_columns= ["customer_id","product_name","sales_date","price", "quantity","total_cost","payment_mode"]
df = pd.DataFrame(columns=reqd_columns)

#5k records
for _ in range(1_000):
    customer_id = random.choice(customer_ids)
    product_name = random.choice(list(product_data.keys()))
    sales_date = input_date
    quantity = random.randint(1,20)
    price = product_data[product_name]
    total_cost = price * quantity
    payment_mode = random.choice(["cash", "UPI"])
    data = [customer_id,product_name,sales_date,price,quantity,total_cost,payment_mode]
    df2 = pd.DataFrame([dict(zip(reqd_columns, data))])
    df = pd.concat([df, df2], ignore_index=True)


# print(df)
df.to_csv(sales_data_file,index=False)

logging.info("Data generated...")

s3_client = S3ClientProvider().get_client()
S3Util.upload_files(s3_client,env_config.get('bucket'),[sales_data_file],env_config.get("s3_source_dir"))