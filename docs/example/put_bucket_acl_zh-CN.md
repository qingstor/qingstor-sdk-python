# Put ACL 示例

## 请求消息体

|    名称    |  类型  | 描述                                                                                                                        |
| :--------: | :----: | :-------------------------------------------------------------------------------------------------------------------------- |
|    acl     |  List  | 支持设置 0 到多个被授权者                                                                                                   |
|  grantee   |  Dict  | 支持 user, group 两种类型，当设置 user 类型时，需要给出 user id；当设置 group 类型时，目前只支持 QS_ALL_USERS，代表所有用户 |
| permission | String | 支持三种权限为 READ, WRITE, FULL_CONTROL                                                                                    |

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

然后您可以 put bucket ACL

```python
acls = [
    {
        "grantee": {
            "type": "user",
            "id": "usr-5OywOXXU"
        },
        "permission": "WRITE"
    },
    {
        "grantee": {
            "type": "group",
            "name": "QS_ALL_USERS"
        },
        "permission": "READ"
    }
]
resp = bucket_srv.put_acl(acl=acls)
if resp.status_code != 200:
    print("Set acl of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name, str(resp.content, 'utf-8')))
else:
    print("Put acl successfully.")
```
