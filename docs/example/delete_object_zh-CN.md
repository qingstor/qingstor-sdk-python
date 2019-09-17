# 删除文件

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

然后调用 `delete_object` 方法删除对象。object_key 设置要删除的对象的 filepath（位于当前 bucket 中）。

```python
object_key = "file_you_want_delete"
output = bucket_srv.delete_object(object_key=object_key)
if output.status_code != 204:
    print("Delete object(name: {}) in bucket({}) failed with given message: {}".format(
        object_key,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    print("Delete success")
```

操作正确返回的话，响应状态码将会是 204。
