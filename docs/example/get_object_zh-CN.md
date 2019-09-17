# 下载对象

## 代码片段

使用您的 AccessKeyID 和 SecretAccessKey 初始化 Qingstor 对象。

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)
```

然后根据要操作的 bucket 信息（zone, bucket name）来初始化 Bucket。

```python
bucket_name = "your-bucket-name"
zone_name = "pek3b"
bucket_srv = qingstor.Bucket(bucket_name, zone_name)
```

想要了解详细的参数信息，可以参考[官方 API 文档](https://docs.qingcloud.com/qingstor/api/object/get)。

然后调用 `get_object` 方法下载对象。object_key 设置要获取的对象的 filepath（位于当前 bucket 中）。

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
