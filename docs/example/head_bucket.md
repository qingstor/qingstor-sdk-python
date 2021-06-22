# Head a Bucket

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

After the object is created, we need to perform the actual Bucket meta information operation:

```python
resp = bucket_srv.head()
if resp.status_code != 200:
    print("Head bucket({}) in zone:{} failed with given message: {}".format(
        bucket_name,
        zone_name,
        str(resp.content, 'utf-8')))
else:
    print("Head bucket successfully.")
```

The function that appears in the code above:
- `bucket_srv.head()` In the `pek3b` area, try to use HEAD to get a Bucket message named `your-bucket-name`.

The object that appears in the above code:
- The `resp` object is the return value of the `bucket_srv.head()` method.
- `resp.status_code` stores the http status code for the api operation.

