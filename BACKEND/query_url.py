from botocore.exceptions import ClientError

# from connection import *
from friendly_url import fri_url


class Query_URL:
    def __init__(self, bucket, b2_resource, is_private=False):
        """
        params:
        key: 文件在b2中的路径信息，如  'your/b2/file.txt'
        b2_resource: b2的connection对象  get_resource
        is_private: default False, 大部分为public bucket， private bucket需要预签名
        """
        self.bucket = bucket
        self.b2_resource = b2_resource
        self.is_private = is_private

    # Return presigned URL of the object in the specified bucket - Useful for *PRIVATE* buckets
    # 预签名的地址，便于打开Private bucket中的文件
    def get_object_presigned_url(self, key, expiration_seconds=3000):
        try:
            response = self.b2_resource.meta.client.generate_presigned_url(ClientMethod='get_object',
                                                                           ExpiresIn=expiration_seconds,  # 验证信息的过期时间
                                                                           Params={
                                                                               'Bucket': self.bucket,
                                                                               'Key': key   # 这个key就是b2上的key_name, 包含了bucket之后的路径信息
                                                                           })
            return response

        except ClientError as ce:
            print('error', ce)

    def list_object_keys(self):
        try:
            # 获取bucket中文件的路径，key
            response = self.b2_resource.Bucket(self.bucket).objects.all()

            return_list = []               # create empty list
            for object in response:        # iterate over response
                # for each item in response append object.key to list
                return_list.append(object.key)
            return return_list             # return list of keys from response

        except ClientError as ce:
            print('error', ce)

    # List browsable URLs of the objects in the specified bucket - Useful for *PUBLIC* buckets

    def list_objects_browsable_url(self, custom_url):
        try:
            # 获取到文件的路径的list（也就是key）
            bucket_object_keys = self.list_object_keys()

            return_list = []                # create empty list
            if self.is_private:  # 如果是私有bucket，调用预签名方法
                for key in bucket_object_keys:
                    url = self.get_object_presigned_url(
                        key, expiration_seconds=3000)
                    return_list.append(url)

            else:  # 公开bucket，直接用friendly_url
                for key in bucket_object_keys:  # iterate bucket_objects
                    # format and concatenate strings as valid url
                    # url = "%s/%s/%s" % (endpoint, bucket, key)
                    url = fri_url(self.bucket, key, custom_url)  # friendly url
                    # for each item in bucket_objects append value of 'url' to list
                    return_list.append(url)

            # print 便于观察
            for i in return_list:
                print(i)
            return return_list              # return list of keys from response

        except ClientError as ce:
            print('error', ce)


# if __name__ == '__main__':
#     BUCKET_NAME = 'ibd-auto'
#     conn = Connection(credentials.ENDPOINT, credentials.KEY_ID,
#                       credentials.APPLICATION_KEY)
#     b2_private = conn.get_b2_resource()
#     URLS = Query_URL(BUCKET_NAME, b2_private)
#     result = URLS.list_objects_browsable_url()
