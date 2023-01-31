import boto3  # REQUIRED!
from botocore.config import Config
from botocore.exceptions import ClientError

# 个人信息
import credentials


# Return a boto3 client object for B2 service
def get_b2_client(endpoint, keyID, applicationKey):
    b2_client = boto3.client(service_name='s3',
                             endpoint_url=endpoint,                 # Backblaze endpoint
                             aws_access_key_id=keyID,               # Backblaze keyID
                             aws_secret_access_key=applicationKey)  # Backblaze applicationKey
    return b2_client

# Return a boto3 resource object for B2 service


def get_b2_resource(endpoint, keyID, applicationKey):
    b2 = boto3.resource(service_name='s3',
                        endpoint_url=endpoint,                    # Backblaze endpoint
                        aws_access_key_id=keyID,                  # Backblaze keyID
                        aws_secret_access_key=applicationKey,     # Backblaze applicationKey
                        config=Config(
                            signature_version='s3v4',
                        ))
    return b2
