# 数据加密

## 代码片段

上传时可对数据进行加密。

访问该链接 [https://docs.qingcloud.com/qingstor/api/common/encryption.html#object-storage-encryption-headers](https://docs.qingcloud.com/qingstor/api/common/encryption.html#object-storage-encryption-headers) .
以更好的理解数据加密解密的过程。

首先，需要初始化 bucket 服务。

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)
bucket_name = "your-bucket-name"
zone_name = "pek3b"
bucket_srv = qingstor.Bucket(bucket_name, zone_name)
```

上传文件时加密。通过设置 `put_object()` 中的相关参数来进行加密操作。

```python
object_key = "your_file_encrypted"
with open("/tmp/your-picture.jpg", "rb") as f:
    output = bucket_srv.put_object(object_key=object_key, 
            x_qs_encryption_customer_algorithm="AES256",
            x_qs_encryption_customer_key="key",
            x_qs_encryption_customer_key_md5="MD5 of the key",
            body=f)
```

下载加密文件需要对文件进行解密，同样是通过设置 input 对应参数。请参考以下示例：

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
