# 删除一个 Bucket

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

对象创建完毕后，我们需要执行真正的删除 Bucket 操作：

```python
resp = bucket_srv.delete()
if resp.status_code != 204:
    print("Delete bucket({}) in zone:{} failed with given message: {}".format(
        bucket_name,
        zone,
        str(resp.content, 'utf-8')))
else:
    print("Delete bucket successfully.")
```

上面代码中出现的函数：
- `bucket_srv.delete()` 在 `pek3b` 区域删除一个名为 `your-bucket-name` 的 Bucket。 

上面代码中出现的对象：
- `resp` 对象是 `bucket_srv.delete()` 方法的返回值。
- `resp.status_code` 存储了 api 操作的 http 状态码。

