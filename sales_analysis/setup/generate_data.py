from datetime import datetime,timedelta
import os
import pandas as pd
import random
import logging
import sys
sys.path.append(os.getcwd())

from resources import env_config

def gen_data():
    #50 customers
    # customer_ids = [str(uuid.uuid4().hex) for _ in range(50)]
    customer_ids = [i for i in range(1,51)]

    #15 stores
    store_ids = [i for i in range(901, 916)]

    product_data = {"apple":100, "banana":20, "orange":30, "bread":50, "milk":150, "cheese":300, "lettuce":80, "chicken":250, "rice":100, "tomato":45}

    sales_persons = {store_id: [j for j in range((i - 1) * 3 + 1, i * 3 + 1)] for i, store_id in enumerate(store_ids, start=1)}

    #Let's generate for 1 year
    start_date = datetime(2023,1,1)
    end_date = datetime(2023,12,31)

    files_path = env_config.get("local_dir")
    sales_data_file = os.path.join(files_path,"sales_data.csv")
    
    reqd_columns= env_config.get('mandatory_cols').split(',')
    df = pd.DataFrame(columns=reqd_columns)

    #5k records
    for _ in range(5_000):
        customer_id = random.choice(customer_ids)
        store_id = random.choice(store_ids)
        product_name = random.choice(list(product_data.keys()))
        sales_date = start_date + timedelta(days=random.randint(0,(end_date-start_date).days))
        sales_person_id = random.choice(sales_persons[store_id])
        quantity = random.randint(1,20)
        price = product_data[product_name]
        total_cost = price * quantity
        data = [customer_id,store_id,product_name,sales_date,sales_person_id,price,quantity,total_cost]
        df2 = pd.DataFrame([dict(zip(reqd_columns, data))])
        df = pd.concat([df, df2], ignore_index=True)


    # print(df)
    df.to_csv(sales_data_file,index=False)

    logging.info("Data is Generated.......")
    return sales_data_file

gen_data()