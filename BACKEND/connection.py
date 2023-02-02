import boto3  # REQUIRED!
from botocore.config import Config


# 个人信息
# import credentials


class Connection:
    def __init__(self, endpoint, keyID, applicationKey):
        self.endpoint = endpoint
        self.keyID = keyID
        self.applicationKey = applicationKey
        # self.custom_url = custom_url
# Return a boto3 client object for B2 service

    def get_b2_client(self):
        b2_client = boto3.client(service_name='s3',
                                 endpoint_url=self.endpoint,                 # Backblaze endpoint
                                 aws_access_key_id=self.keyID,               # Backblaze keyID
                                 aws_secret_access_key=self.applicationKey)  # Backblaze applicationKey
        return b2_client

    # Return a boto3 resource object for B2 service

    def get_b2_resource(self):
        b2_resource = boto3.resource(service_name='s3',
                                     endpoint_url=self.endpoint,                    # Backblaze endpoint
                                     aws_access_key_id=self.keyID,                  # Backblaze keyID
                                     aws_secret_access_key=self.applicationKey,     # Backblaze applicationKey
                                     config=Config(
                                         signature_version='s3v4',
                                     ))
        return b2_resource


# if __name__ == '__main__':
#     conn = Connection(credentials.ENDPOINT, credentials.KEY_ID,
#                       credentials.APPLICATION_KEY)
