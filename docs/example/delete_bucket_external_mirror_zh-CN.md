# DELETE Bucket External Mirror

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

然后您可以 DELETE Bucket External Mirror

```python
resp = bucket_srv.delete_external_mirror()
if resp.status_code != 204:
    print("Delete external mirror of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name,
        str(resp.content, 'utf-8')))
else:
    print("Delete external mirror successfully.")
```
