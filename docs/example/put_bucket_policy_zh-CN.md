# PUT Bucket Policy

## 请求消息体

访问 [API Docs](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/bucket/policy/put_policy/) 以查看更多关于请求消息体的信息。

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

然后您可以 put bucket Policy

```python
stmts = [
    {
        "id": "allow certain site to get objects",
        "user": "*",
        "action": ["get_object"],
        "effect": "allow",
        "resource": [bucket_name + "/*"],
        "condition": {
            "string_like": {
                "Referer": [
                    "*.example1.com",
                    "*.example2.com"
                ]
            }
        }
    },
]
resp = bucket_srv.put_policy(statement=stmts)
if resp.status_code != 200:
    print("Set policy of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name, str(resp.content, "utf-8")))
else:
    print("Put bucket policy successfully.")
```
