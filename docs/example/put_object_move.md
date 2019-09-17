# MoveObject Example

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

Then set the input parameters used by the PutObject method (core parameter: XQSMoveSource).
For parameter details, please refer to [Official API Documentation](https://docs.qingcloud.com/qingstor/api/object/move).

Then call the `put_object` method to move the object. object_key Sets the filepath after put (in the current bucket).

```python
obj_of_bucket = "/your-bucket-name/your-picture-uploaded.jpg"
source = parse.quote(obj_of_bucket, safe="/")
target = "file-moved/your-picture-moved.jpg"  # file and directory created automatically.
output = bucket_srv.put_object(object_key=target, x_qs_move_source=source)
if output.status_code != 201:
    print("Move object(name: {}) to bucket({}) failed with given message: {}".format(
        obj_of_bucket,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    print("Copy success")
```
