import credentials


credentials.Info('shirley').CUSTOM_URL


def fri_url(BUCKET_NAME, key, CUSTOM_URL):
    # key 是一个 remote/path/file.xxx这样的字符串
    # BASE_URL = credentials.Info('shirly').CUSTOM_URL
    FULL_URL = CUSTOM_URL + BUCKET_NAME + '/' + key
    # print(FULL_URL)
    return FULL_URL
