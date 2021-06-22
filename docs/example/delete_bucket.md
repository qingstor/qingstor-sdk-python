# Delete a Bucket

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

After created the object, we need perform the action to delete a Bucket：

```python
resp = bucket_srv.delete()
if resp.status_code != 204:
    print("Delete bucket({}) in zone:{} failed with given message: {}".format(
        bucket_name,
        zone_name,
        str(resp.content, 'utf-8')))
else:
    print("Delete bucket successfully.")
```

The function that appears in the code above:
- `bucket_srv.delete()` Deletes a Bucket named `your-bucket-name` in the `pek3b` field.

The object that appears in the above code:
- The `resp` object is the return value of the `bucket_srv.delete()` method.
- `resp.status_code` stores the http status code for the api operation.

