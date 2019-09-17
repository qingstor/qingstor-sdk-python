# GET Bucket ACL

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

对象创建完毕后，我们需要执行真正的获取 Bucket ACL 操作：

```python
resp = bucket_srv.get_acl()
if resp.status_code != 200:
    print("Get acl of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name, str(resp.content, 'utf-8')))
else:
    print("The bucket acl info:")
    print(resp['acl'])
```
