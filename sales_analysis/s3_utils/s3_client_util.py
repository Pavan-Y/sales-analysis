import logging
from datetime import datetime,timezone
import os

class S3Util:
    
    def list_files(s3_client,bucket,file_path,start_ts=None,end_ts=None):
        try:
            response = s3_client.list_objects_v2(Bucket=bucket,Prefix=file_path)
            if 'Contents' in response:
                logging.info(f"Files available in {bucket} with prefix {file_path} are {response['Contents']}")
                if start_ts or end_ts:
                    start_ts=datetime(2000, 1, 1, 0, 0, 0,tzinfo=timezone.utc) if not start_ts else start_ts
                    end_ts =datetime.now(timezone.utc) if not end_ts else end_ts
                    files = [str(obj['Key']) for obj in response['Contents'] if obj['LastModified']>=start_ts and obj['LastModified']<=end_ts]
                else:
                    files = [str(obj['Key']) for obj in response['Contents']]
                return files
            logging.error("No files available in s3")
            return []
        except Exception as e:
            logging.exception(f"unknown exception, {e}")
            
    def download_files(s3_client,bucket,files_list,local_dir):
        for file in files_list:
            file_name = os.path.basename(file)
            download_path = os.path.join(local_dir,file_name)
            try:
                s3_client.download_file(bucket,file,download_path)
            except Exception as e:
                logging.exception(f"Error while downloading {file} -> {e}")
        logging.info("Downloading is done.")
    
    def upload_files(s3_client,bucket,files_list,folder_path,directory=None):
        if directory:
            current_epoch = int(datetime.now().timestamp()) * 1000
            s3_prefix = f"{files_list.split('/')[-1]}/{current_epoch}"
            for root, dirs, files in os.walk(files_list):
                for file in files:
                    local_file_path = os.path.join(root, file)
                    s3_key = f"{s3_prefix}/{file}"
                    s3_client.upload_file(local_file_path, bucket, s3_key)
            return f"Data Successfully uploaded in {directory} data mart "
        for file in files_list:
            file_name = os.path.basename(file)
            s3_key = os.path.join(folder_path,file_name) #folder path is prefix here
            try:
                s3_client.upload_file(file,bucket,s3_key)
            except Exception as e:
                logging.exception(f"Error while uploading {file} -> {e}")
        logging.info("Uploading is done.")
        
    def move_files(s3_client,bucket,src_prefix,dest_prefix,file_name=None):
        try:
            response = s3_client.list_objects_v2(Bucket=bucket,Prefix=src_prefix)
            if not file_name:
                for obj in response['Contents']:
                    src_key = obj['Key']
                    dest_key = dest_prefix+ src_key[len(src_prefix):]
                    
                    s3_client.copy_object(Bucket=bucket,CopySource={'Bucket':bucket,'Key':src_key},Key=dest_key)
                    
                    s3_client.delete_object(Bucket=bucket,Key=src_key)
            else:
                for obj in response.get('Contents', []):
                    src_key = obj['Key']
                    print(src_key,file_name)
                    if src_key.endswith(os.path.basename(file_name)):
                        dest_key = dest_prefix + src_key[len(src_prefix):]

                        s3_client.copy_object(Bucket=bucket,CopySource={'Bucket': bucket,'Key': src_key}, Key=dest_key)

                        s3_client.delete_object(Bucket=bucket, Key=src_key)
                        logging.info(f"Moved file: {src_key} to {dest_key}")
            logging.info("Moved successfully.")
        except Exception as e:
            logging.exception(f"Moving failed due to {e}")