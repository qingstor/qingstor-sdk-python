# 对象移动

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

然后设置 PutObject 方法用到的输入参数（核心参数：XQSMoveSource）。
想要了解详细的参数信息，可以参考[官方 API 文档](https://docs.qingcloud.com/qingstor/api/object/move)。

然后调用 `put_object` 方法移动对象。object_key 设置 put 后的 filepath（位于当前 bucket 中）。

```python
obj_of_bucket = "/your-bucket-name/your-picture-uploaded.jpg"
source = parse.quote(obj_of_bucket, safe="/")
target = "file-moved/your-picture-moved.jpg"  # file and directory created automatically.
output = bucket_srv.put_object(object_key=target, x_qs_move_source=source)
if output.status_code != 201:
    print("Move object(name: {}) to bucket({}) failed with given message: {}".format(
        obj_of_bucket,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    print("Copy success")
```
