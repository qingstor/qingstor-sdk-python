# PUT Object - Fetch

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

Then set the input parameters used by the PutObject method (core parameter: XQSFetchSource).
For parameter details, please refer to [Official API Documentation](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/fetch/).

Then call the `put_object` method to fetch object. object_key Sets the filepath after put (in the current bucket).

```python
source = "https://www.qingcloud.com/static/assets/images/icons/common/footer_logo.svg"
target = "file-fetched/the_file_fetched.svg"  # file and directory created automatically.
output = bucket_srv.put_object(object_key=target, x_qs_fetch_source=source)
if output.status_code != 201:
    print("Fetch url:({}) to path:({}) in bucket({}) failed with given message: {}".format(
        source,
        target,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    print("Fetch success")
```
