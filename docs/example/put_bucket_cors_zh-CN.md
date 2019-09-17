# PUT Bucket CORS

## 请求消息体

|      名称       |  类型   | 描述                                                                                                            | 是否必要 |
| :-------------: | :-----: | :-------------------------------------------------------------------------------------------------------------- | :------: |
|   cors_rules    |  Array  | 跨源的规则配置，每组配置项中的元素解释如下。                                                                    |   Yes    |
| allowed_origin  | String  | 用户所期望的跨源请求来源,可以用 ‘*’ 来进行通配。                                                                |   Yes    |
| allowed_methods |  Array  | 设置源所允许的 HTTP 方法。可指定以下值的组合: “GET”, “PUT”, “POST”, “DELETE”, “HEAD”, 或者使用 ‘*’ 来进行设置。 |   Yes    |
| allowed_headers |  Array  | 设置源所允许的 HTTP header 。 可以用 ‘*’ 来进行通配。                                                           |    No    |
| expose_headers  |  Array  | 设置客户能够从其应用程序（例如，从 JavaScript XMLHttpRequest 对象）进行访问的HTTP 响应头。                      |    No    |
| max_age_seconds | Integer | 设置在预检请求(Options)被资源、HTTP 方法和源识别之后，浏览器将为预检请求缓存响应的时间（以秒为单位）。          |    No    |

访问 [API Docs](https://docs.qingcloud.com/qingstor/api/bucket/cors/put_cors.html) 以查看更多关于请求消息体的信息。

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

然后您可以 PUT Bucket CORS

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
