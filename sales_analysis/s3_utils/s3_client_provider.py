import boto3
import os
from botocore.exceptions import NoCredentialsError
import logging
from dotenv import load_dotenv

class S3ClientProvider:
    def __init__(self,aws_access_key=None, aws_secret_key=None) -> None:
        load_dotenv()
        self.aws_access_key = aws_access_key if aws_access_key else os.environ.get('access_key')
        self.aws_secret_key = aws_secret_key if aws_secret_key else os.environ.get('secret_key')
        try:
            self.session = boto3.Session(aws_access_key_id=self.aws_access_key,aws_secret_access_key=self.aws_secret_key)
        except NoCredentialsError as ex:
            logging.error("Update the environemnt file")
            raise ex
        self.s3_client = self.session.client('s3')
        
    def get_client(self):
        return self.s3_client
