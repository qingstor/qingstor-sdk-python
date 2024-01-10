`# PutObjects Example

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

Then set the input parameters that the PutObject method might use. For parameter details, please refer to [Official API Documentation](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/put/).

Then call the `put_object` method to upload the object. object_key Sets the filepath after uploading.

```python
filepath = "/tmp/your-picture.jpg"
content_md5 = calculate_md5(filepath)
object_key = "your-picture-uploaded.jpg"
with open(filepath, "rb") as f:
    output = bucket_srv.put_object(object_key=object_key, content_type="image/jpeg",
                                        content_md5=content_md5,
                                        x_qs_storage_class="STANDARD", body=f)
if output.status_code != 201:
    print("Upload object(name: {}) to bucket({}) failed with given message: {}".format(
        object_key,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    print("Upload success")
```

```python
import hashlib

def calculate_md5(filepath) -> str:
    h = hashlib.md5()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()
```
`
