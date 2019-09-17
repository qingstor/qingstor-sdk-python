# OPTIONS Object

## api 信息

### 请求头(Request Headers)

|              名称              |  类型  | 描述                                           | 是否必要 |
| :----------------------------: | :----: | :--------------------------------------------- | :------: |
|             Origin             | String | 跨源请求的源。                                 |   Yes    |
| Access-Control-Request-Method  | String | 跨源请求的 HTTP method 。                      |   Yes    |
| Access-Control-Request-Headers | String | 跨源请求中的 HTTP headers (逗号分割的字符串)。 |    No    |

访问 [API Docs](https://docs.qingcloud.com/qingstor/api/object/options.html) 以查看更多关于请求头的信息。

### 响应头(Response Headers)

|             名称              |  类型  | 描述                                                                                           |
| :---------------------------: | :----: | :--------------------------------------------------------------------------------------------- |
|  Access-Control-Allow-Origin  | String | 跨源请求所允许的源。如果跨源请求没有被允许，该头信息将不会存在于响应头中。                     |
|    Access-Control-Max-Age     | String | 预检请求的结果被缓存的时间（单位为秒）。                                                       |
| Access-Control-Allow-Methods  | String | 跨源请求中的 HTTP method 。如果跨源请求没有被允许，该头信息将不会存在于响应头中。              |
| Access-Control-Allow-Headers  | String | 跨源请求中可以被允许发送的 HTTP headers (逗号分割的字符串)。                                   |
| Access-Control-Expose-Headers | String | 跨源请求的响应中,客户端（如 JavaScript Client） 可以获取到的 HTTP headers (逗号分割的字符串)。 |

访问 [API Docs](https://docs.qingcloud.com/qingstor/api/object/options.html) 以查看更多关于响应头的信息。

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

然后设置 OptionsObject 方法用到的输入参数并调用 `options_object` 方法。
object_key 设置要 options 的对象的 filepath（位于当前 bucket 中）。

```python
object_key = "your_file_test_options.zip"
output = bucket_srv.options_object(object_key=object_key,
                                        access_control_request_headers="content-length,content-type",
                                        access_control_request_method="DELETE,GET,PUT,PATCH",
                                        origin="http://*.qingcloud.com")
if output.status_code != 200:
    print("options object(name: {}) in bucket({}) failed with given message: {}".format(
        object_key,
        bucket_name,
        str(output.content, 'utf-8')))
else:
    header = output.headers
    # if no cors settings on this bucket, headers will include nothing about following header keys.
    print(header.get('Access-Control-Allow-Headers'))
    print(header.get('Access-Control-Expose-Headers'))
    print(header.get('Access-Control-Allow-Methods'))
    print(header.get('Access-Control-Max-Age'))
    print(header.get('Access-Control-Allow-Origin'))
```

想要了解详细的参数信息，可以参考[官方 API 文档](https://docs.qingcloud.com/qingstor/api/object/options)。

响应将返回过滤过后的所有被允许的操作（包括 header, method, origin）。
