# PUT Bucket CORS

## Request Elements

|      Name       |  Type   | Description                                                                                                                                                                        | Required |
| :-------------: | :-----: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: |
|   cors_rules    |  Array  | A set of origins and methods (cross-origin access that you want to allow). The elements in each set of configuration items are explained as follows.                               |   Yes    |
| allowed_origin  | String  | An origin that you want to allow cross-domain requests from. This can contain at most one * wild character.                                                                        |   Yes    |
| allowed_methods |  Array  | An HTTP method that you want to allow the origin to execute. A combination of the following values can be specified: “GET”, “PUT”, “POST”, “DELETE”, “HEAD”, or use ‘*’ to set up. |   Yes    |
| allowed_headers |  Array  | An HTTP header that you want to allow the origin to execute. This can contain at most one * wild character.                                                                        |    No    |
| expose_headers  |  Array  | One or more headers in the response that you want customers to be able to access from their applications (for example, from a JavaScript XMLHttpRequest object).                   |    No    |
| max_age_seconds | Integer | The time in seconds that your browser is to cache the preflight response for the specified resource.(seconds)                                                                      |    No    |

See [API Docs](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/bucket/cors/put_cors/) for more information about request elements.

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

then you can PUT Bucket CORS

```python
cors_rules = [
    {
        "allowed_origin": "http://*.qingcloud.com",
        "allowed_methods": [
            "PUT", "GET", "POST", "DELETE"
        ],
        "allowed_headers": [
            "x-qs-date", "Content-Type", "Content-MD5", "Authorization"
        ],
        "max_age_seconds": 200,
        "expose_headers": [
            "x-qs-date"
        ]
    }
]
resp = bucket_srv.put_cors(cors_rules=cors_rules)
if resp.status_code != 200:
    print("Set CORS of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name, str(resp.content, "utf-8")))
else:
    print("Put bucket CORS successfully.")
```
