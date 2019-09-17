# DeleteObject Example

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

Then call the `delete_object` method to delete the object. object_key Sets the filepath of the object to be deleted (in the current bucket).

```python
object_key = "file_you_want_delete"
output = bucket_srv.delete_object(object_key=object_key)
if output.status_code != 204:
    print("Delete object(name: {}) in bucket({}) failed with given message: {}".format(
        object_key,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    print("Delete success")
```

If the operation returns correctly, the response status code will be 204.
