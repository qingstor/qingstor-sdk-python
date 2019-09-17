# PUT Bucket Policy

## Request Elements

See [API Docs](https://docs.qingcloud.com/qingstor/api/bucket/policy/put_policy.html) for more information about request elements.

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

then you can put Bucket Policy

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
