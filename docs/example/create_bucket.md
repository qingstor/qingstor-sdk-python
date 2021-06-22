# Create a Bucket

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

The `bucket_srv` object is used to manipulate the Bucket and can use all Bucket and Object level APIs. Now perform the real creation of the Bucket operation:

```python
resp = bucket_srv.put()
if resp.status_code != 201:
    print("Create bucket({}) in zone:{} failed with given message: {}".format(
        bucket_name,
        zone_name,
        str(resp.content, 'utf-8')))
else:
    print("Create bucket successfully.")
```

`bucket_srv.put()` will create a Bucket in the specified zone.

