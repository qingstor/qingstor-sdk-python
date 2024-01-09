# GetObject Example

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

For parameter details, please refer to [Official API Documentation](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/get/).

Then call the `get_object` method to download the object. object_key Sets the filepath of the object to be fetched (in the current bucket).

```python
import tempfile

object_key = "your-picture-uploaded.jpg"
output = bucket_srv.get_object(object_key=object_key)
if output.status_code != 200:
    print("Get object(name: {}) in bucket({}) failed with given message: {}".format(
        object_key,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    # example: stored in /tmp folder.
    with tempfile.NamedTemporaryFile(delete=False) as f:
        for chunk in output.iter_content():
            f.write(chunk)
        print(f.name)
```
