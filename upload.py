from botocore.exceptions import ClientError

# from connection import *
from friendly_url import fri_url
import os

# Upload specified file into the specified bucket


# b2path是完整上传路径xx/xx/xx  路径开头和最后都不要'/'
def upload_file(bucket, directory, file, b2, b2path=None):
    # file_path = directory + '/' + file
    file_path = os.path.join(directory, file)
    remote_path = b2path
    if remote_path is None:
        remote_path = file
    else:
        remote_path = b2path + '/' + file
    try:
        response = b2.Bucket(bucket).upload_file(file_path, remote_path)
    except ClientError as ce:
        print('error', ce)

    friendly_url = fri_url(bucket, remote_path)

    return response


# if __name__ == '__main__':
#     LOCAL_DIR = os.getcwd()
#     file = 'test_file.txt'
#     TARGET_BUCKET = 'kmoretop-blog'

#     conn = Connection(credentials.ENDPOINT, credentials.KEY_ID,
#                       credentials.APPLICATION_KEY)
#     b2_resource = conn.get_b2_resource()
#     response = upload_file(TARGET_BUCKET, LOCAL_DIR,
#                            file, b2_resource, 'test')
#     print('RESPONSE:  ', response)
