# GetDownObjectMulti Example

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

The parameter that must be set manually here is the range parameter. For parameter details, please refer to [Official API Documentation](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/get/).

Then call the `get_object` method to download the object and set 5M as the segment size. object_key sets the filepath of the object to be fetched (in the current bucket).

```python
object_key = "your_zip_fetch_with_seg.zip"
part_size = 1024 * 1024 * 5  # 5M every part.
# ensure the file we will write to does not exists.
if os.path.exists("/tmp/" + object_key):
    os.remove("/tmp/" + object_key)
i = 0
while True:
    lo = part_size * i
    hi = part_size * (i + 1) - 1
    byte_range = "bytes=%d-%d" % (lo, hi)
    output = bucket_srv.get_object(object_key=object_key, range=byte_range)
    if output.status_code != 206:
        print("Get object(name: {}) by segment in bucket({}) failed with given message: {}".format(
            object_key,
            bucket_name,
            str(output.content, 'utf-8')))
        os.remove("/tmp/" + object_key)
        break
    else:
        with open("/tmp/" + object_key, 'a+b') as f:  # append to file in binary mode
            f.write(output.content)
        if len(output.content) < part_size:
            break
        i += 1
```

The file will be saved to /tmp/{object_key} (replace with your object_key).
