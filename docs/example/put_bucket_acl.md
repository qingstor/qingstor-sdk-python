# PutACL Example

## Request Elements

|    Name    |  Type  | Description                                                                                                                        |
| :--------: | :----: | :--------------------------------------------------------------------------------------------------------------------------------- |
|    acl     |  List  | Supports to set 0 or more grantees                                                                                                 |
|  grantee   |  Dict  | Specifies the Type(user, group). When type is user, need user id; when type is group, only supports QS_ALL_USERS(all of the users) |
| permission | String | Specifies the permission (READ, WRITE, FULL_CONTROL) given to the grantee.                                                         |

## Code Snippet

Initialize the Qingstor object with your AccessKeyID and SecretAccessKey.

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)
```

Initialize a Bucket object according to the bucket name you set for subsequent creation:

```python
bucket_name = "your-bucket-name"
zone_name = "pek3b"
bucket_srv = qingstor.Bucket(bucket_name, zone_name)
```

then you can put bucket ACL

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
