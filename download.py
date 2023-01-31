
from botocore.exceptions import ClientError

# from connection import *
import os
import credentials


# Download the specified object from B2 and write to local file system
def download_file(bucket, directory, local_name, key_name, b2):
    file_path = os.path.join(directory, local_name)
    try:
        b2.Bucket(bucket).download_file(key_name, file_path)
    except ClientError as ce:
        print('error', ce)


# if __name__ == '__main__':
#     conn = Connection(credentials.ENDPOINT, credentials.KEY_ID,
#                       credentials.APPLICATION_KEY)
#     b2_resource = conn.get_b2_resource()

#     LOCAL_DIR = os.getcwd()
#     file = 'test_file.txt'
#     FROM_BUCKET = 'kmoretop-blog'

#     key_name = 'test/'+file  # key_name 需要带bucket中的路径文件夹，xxx/file.xx，头尾不带'/'

#     download_file(bucket=FROM_BUCKET, directory=LOCAL_DIR,
#                   local_name=file, key_name=key_name, b2=b2_resource)
