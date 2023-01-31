from get_list import *
from query_url import *
from download import *
from upload import *
from connection import *

conn = Connection(credentials.ENDPOINT, credentials.KEY_ID,
                  credentials.APPLICATION_KEY)
b2_client = conn.get_b2_client()
a = list_buckets(b2_client=b2_client)
print(a)
