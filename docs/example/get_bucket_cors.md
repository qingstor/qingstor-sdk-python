# GET Bucket CORS

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

then you can GET Bucket CORS

```python
resp = bucket_srv.get_cors()
if resp.status_code != 200:
    print("Get CORS of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name, str(resp.content, 'utf-8')))
else:
    print("The bucket CORS info:")
    print(resp['cors_rules'])
```
