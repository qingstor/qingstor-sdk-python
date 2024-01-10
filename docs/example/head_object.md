# HEAD Object

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

For parameter details, please refer to [Official API Documentation](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/head/).

Then call the `head_object` method to get the object meta information and test if it can be accessed. object_key Sets the filepath of the object to be fetched (in the current bucket).

```python
object_key = "your-picture-uploaded.jpg"
output = bucket_srv.head_object(object_key=object_key)
if output.status_code != 200:
    print("Get metadata of object(name: {}) in bucket({}) failed with given message: {}".format(
        object_key,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    # check all useful headers related to object info in: https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/head/
    print(output.headers['ETag'])
    print(output.headers['Content-Type'])
```

If the operation returns correctly, the response status code will be 200.
