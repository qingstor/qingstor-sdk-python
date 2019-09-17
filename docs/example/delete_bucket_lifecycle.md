# DELETE Bucket Lifecycle

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

then you can DELETE Bucket Lifecycle

```python
resp = bucket_src.delete_lifecycle()
if resp.status_code != 204:
    print("Delete lifecycle of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name,
        str(resp.content, 'utf-8')))
else:
    print("Delete lifecycle successfully.")
```
