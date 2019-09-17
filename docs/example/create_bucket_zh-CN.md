# 创建一个 Bucket

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

`bucket_srv` 对象用于操作 Bucket，可以使用所有 Bucket 和 Object 级别的 API。现在执行真正的创建 Bucket 操作：

```python
resp = bucket_srv.put()
if resp.status_code != 201:
    print("Create bucket({}) in zone:{} failed with given message: {}".format(
        bucket_name,
        zone,
        str(resp.content, 'utf-8')))
else:
    print("Create bucket successfully.")
```

`bucket_srv.put()` 会在指定 zone 创建 Bucket。 

