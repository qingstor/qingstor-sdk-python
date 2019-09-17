# Get Bucket Statistics

## Code Snippet

Initialize the Qingstor object with your AccessKeyID and SecretAccessKey.

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)
```

Initialize a Bucket object according to the bucket name you set for subsequent creation:

```python
bucket_name = "your-bucket-name"
zone_name = "pek3b"
bucket_srv = qingstor.Bucket(bucket_name, zone_name)
```

After the object is created, we need to perform the actual Bucket usage statistics:

```python
resp = bucket_srv.get_statistics()
if resp.status_code != 200:
    print("Get statistics of bucket({}) failed with given message: {}".format(
        bucket_name,
        str(resp.content, 'utf-8')))
else:
    print("The bucket statistics:")
    print(str(resp.content, encoding='utf-8'))
    # print("Bucket info: {size: %d, count: %d, location: %s, url: %s, created: %s}\n" % (
    #     resp['size'], resp['count'], resp['location'], resp['url'], resp['created']))
```

