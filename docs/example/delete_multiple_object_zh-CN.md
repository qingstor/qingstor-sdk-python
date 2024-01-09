# 删除多个对象

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

然后设置 `delete_multiple_objects` 方法用到的输入参数。`quiet` 指定是否返回被删除的对象列表。

```python
objects = [{"key": "file_will_be_delete.jpg"}, {"key": "file_will_be_delete.zip"}]
```

想要了解详细的参数信息，可以参考[官方 API 文档](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/bucket/basic_opt/delete_multiple/)。

然后调用 `delete_multiple_objects` 方法删除对象。object_key 设置要删除的对象的 filepath（位于当前 bucket 中）。

```python
output = bucket_srv.delete_multiple_objects(objects=objects, quiet=False)
if output.status_code != 200:
    print("Delete objects({}) in bucket({}) failed with given message: {}".format(
        objects,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    print(output['deleted'])  # 'deleted' contains objects deleted successfully.
```

操作正确返回的话，响应状态码将会是 200。
