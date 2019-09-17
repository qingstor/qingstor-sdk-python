# CopyObject Example

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

Then set the input parameters used by the PutObject method (core parameter: XQSCopySource). 
For parameter details, please refer to [Official API Documentation](https://docs.qingcloud.com/qingstor/api/object/copy).

Then call the PutObject method to copy the object. object_key Sets the copied filepath (located in the current bucket).

```python
from urllib import parse

# Please replace this path with some file exists on your bucket.
# format: /source-bucket/source-object
# notice that path should be url encoded but with "/" reserved.
obj_of_bucket = "/your-bucket-name/your-picture-uploaded.jpg"
source = parse.quote(obj_of_bucket, safe="/")
target = "file-copied/file-copied.jpg"  # file and directory created automatically.
output = bucket_srv.put_object(object_key=target, x_qs_copy_source=source)
if output.status_code != 201:
    print("Copy object(name: {}) to bucket({}) failed with given message: {}".format(
        obj_of_bucket,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    print("Copy success")
```
