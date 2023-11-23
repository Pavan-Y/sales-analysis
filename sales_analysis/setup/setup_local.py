import os
import sys
from botocore.exceptions import ClientError
sys.path.append(os.getcwd())

from sales_analysis.spark_utils.session_provider import get_mysql_session
from sales_analysis.s3_utils.s3_client_provider import S3ClientProvider
from sqlalchemy import text
from resources import env_config
from generate_data import gen_data
from sales_analysis.s3_utils.s3_client_util import S3Util

def db_setup():
    #create db(db name in config)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    queries_file = os.path.join(current_dir, 'sql_queries.sql')

    with open(queries_file,'r') as q:
        sql_queries = q.read()
        
    queries = sql_queries.split(';')

    engine = get_mysql_session()
    with engine.connect() as conn:
        for query in queries:
            if query.strip():
                conn.execute(text(query.replace('my-bucket-name',env_config.get("bucket"))))
    print("done")
    
def aws_setup():
    s3_client = S3ClientProvider().get_client()
    try:
        s3_client.head_bucket(Bucket=env_config.get('bucket'))
    except ClientError as c:
        if c.response['Error']['Code'] == '404':
            print("Bucket doesn't exist. Creating...")
            s3_client.create_bucket(Bucket=env_config.get('bucket'))
            print("Bucket created.")
        else:
            print(f"Error: {c}")

def populate_s3():
    #ideally this data comes from the application.. here we're generating it and uploading it to s3
    file = gen_data()
    s3_client = S3ClientProvider().get_client()
    S3Util.upload_files(s3_client,env_config.get('bucket'),[file],env_config.get("s3_source_dir"))
    print("Populated data to S3.")
    
# db_setup()
# aws_setup()
# populate_s3()

#mysql jar is required to connect to mysql db with spark
#https://downloads.mysql.com/archives/c-j/
#platform independent jar -> keep this under jars/of SPARK_HOME

#You can test this programme by generating data with more/less columns using scripts available under test/