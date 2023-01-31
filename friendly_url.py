import credentials


def fri_url(BUCKET_NAME, key):
    # remote_path 是一个 remote/path/file.xxx这样的字符串
    BASE_URL = credentials.CUSTOM_URL
    FULL_URL = BASE_URL + BUCKET_NAME + '/' + key
    # print(FULL_URL)
    return FULL_URL
