# Encryption Example

### Code Snippet

You can encrypt data when uploading.

To understand the process of encryption better, visit the link [https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/encryption/](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/encryption/) .

First, initialize the bucket service.

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)
bucket_name = "your-bucket-name"
zone_name = "pek3b"
bucket_srv = qingstor.Bucket(bucket_name, zone_name)
```

Encrypt when uploading files. The encryption operation is performed by setting related items in `put_object` method.

```python
object_key = "your_file_encrypted"
with open("/tmp/your-picture.jpg", "rb") as f:
    output = bucket_srv.put_object(object_key=object_key,
            x_qs_encryption_customer_algorithm="AES256",
            x_qs_encryption_customer_key="key",
            x_qs_encryption_customer_key_md5="MD5 of the key",
            body=f)
```

Downloading an encrypted file requires decrypting the file. It also need set the input parameter. Please refer to the following example:

```python
import tempfile

object_key = "your_file_encrypted"
output = bucket_srv.get_object(object_key=object_key,
            x_qs_encryption_customer_algorithm="AES256",
            x_qs_encryption_customer_key="key",
            x_qs_encryption_customer_key_md5="MD5 of the key")
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
