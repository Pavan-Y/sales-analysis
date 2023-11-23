import os
import sys
sys.path.append(os.getcwd())

from sales_analysis.s3_utils.s3_client_provider import S3ClientProvider
from sales_analysis.s3_utils.s3_client_util import S3Util
from resources import env_config


def upload_local_data(path=None):
    if path:
        local_dir = path
    else:
        print(env_config.get("local_dir"))
        local_dir = os.path.join(os.getcwd(),env_config.get("local_dir"))
    for root,dir,files in os.walk(local_dir):
        files = [os.path.join(root, file) for file in files]
        print(files,root)
        s3_client = S3ClientProvider().get_client()
        S3Util.upload_files(s3_client,env_config.get("bucket"),files,env_config.get("s3_source_dir"))
            
upload_local_data()