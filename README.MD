BlackBlaze OSS storage

### Code Source

https://github.com/backblaze-b2-samples/b2-python-s3-sample/

It's an official B2 sample code. From the `sample.py` file, lots of practice can be leanrt.

### My Code

1. I separated different functions in to `py` files.
2. I didn't apply `python-dotenv` package, instead, I choose to use a `credentials.py`, which looks like this:

```python
/credentials.py

# B2 API endpoint for buckets with sample data
ENDPOINT = 'https://s3.us-west-004.backblazeb2.com'


# Credentials
KEY_ID = 'your key ID'
APPLICATION_KEY = 'Your Application ID'

# Custom Domains or given b2 friendly url
# If just domains, you need to write until '/file/', aka, before the bucket name

CUSTOM_URL = 'https://f004.backblazeb2.com/file/'


```

### To-dos

A GUI or CMD-line needed. GUI will be better, especially with dropdowns.
