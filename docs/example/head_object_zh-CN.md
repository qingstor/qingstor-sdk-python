# 获取文件的元数据

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

想要了解详细的参数信息，可以参考[官方 API 文档](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/head/)。

然后调用 `head_object` 方法获取对象元信息，测试是否可以被访问。object_key 设置要获取的对象的 filepath（位于当前 bucket 中）。

```python
object_key = "your-picture-uploaded.jpg"
output = bucket_srv.head_object(object_key=object_key)
if output.status_code != 200:
    print("Get metadata of object(name: {}) in bucket({}) failed with given message: {}".format(
        object_key,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    # check all useful headers related to object info in: https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/head/
    print(output.headers['ETag'])
    print(output.headers['Content-Type'])
```

操作正确返回的话，响应状态码将会是 200。
