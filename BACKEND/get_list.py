from botocore.exceptions import ClientError

# from connection import *


def list_buckets(b2_client, raw_object=False):
    # 把账号里的buckets都列出来
    try:
        my_buckets_response = b2_client.list_buckets()   # 输出是一个字典

        print('\nBUCKETS')
        return_list = []
        for bucket_object in my_buckets_response['Buckets']:
            print(bucket_object['Name'])
            return_list.append(bucket_object['Name'])

        if raw_object:
            print('\nFULL RAW RESPONSE:')
            print(my_buckets_response)

        return return_list

    except ClientError as ce:
        print('error', ce)


# if __name__ == '__main__':
#     conn = Connection(credentials.ENDPOINT, credentials.KEY_ID,
#                       credentials.APPLICATION_KEY)
#     b2_client = conn.get_b2_client()
#     list_buckets(b2_client=b2_client)
