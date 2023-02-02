from get_list import *
from query_url import *
from download import *
from upload import *
from connection import *
import credentials

ENDPOINT = credentials.Info('kent').ENDPOINT
KEY_ID = credentials.Info('kent').KEY_ID
APPLICATION_KEY = credentials.Info('kent').APPLICATION_KEY
CUSTOM_URL = credentials.Info('kent').CUSTOM_URL


conn = Connection(ENDPOINT, KEY_ID, APPLICATION_KEY)

b2_client = conn.get_b2_client()
a = list_buckets(b2_client=b2_client)
print(a)
