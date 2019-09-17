# OPTIONS Object

## Request Headers

|              Name              |  Type  | Description                                                                     | Required |
| :----------------------------: | :----: | :------------------------------------------------------------------------------ | :------: |
|             Origin             | String | Identifies the origin of the cross-origin request.                              |   Yes    |
| Access-Control-Request-Method  | String | Identifies what HTTP method will be used in the actual request.                 |   Yes    |
| Access-Control-Request-Headers | String | A comma-delimited list of HTTP headers that will be sent in the actual request. |    No    |

See [API Docs](https://docs.qingcloud.com/qingstor/api/object/options.html) for more information about request headers.

## Response Headers

|             Name              |  Type  | Description                                                                                                                                                                                                                                                                     |
| :---------------------------: | :----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|  Access-Control-Allow-Origin  | String | The origin you sent in your request. If the origin in your request is not allowed, QingStor will not include this header in the response.                                                                                                                                       |
|    Access-Control-Max-Age     | String | How long, in seconds, the results of the preflight request can be cached.                                                                                                                                                                                                       |
| Access-Control-Allow-Methods  | String | The HTTP method that was sent in the original request. If the method in the request is not allowed, QingStor will not include this header in the response.                                                                                                                      |
| Access-Control-Allow-Headers  | String | A comma-delimited list of HTTP headers that the browser can send in the actual request. If any of the requested headers is not allowed, QingStor will not include that header in the response, nor will the response contain any of the headers with the Access-Control prefix. |
| Access-Control-Expose-Headers | String | A comma-delimited list of HTTP headers. This header provides the JavaScript client with access to these headers in the response to the actual request.                                                                                                                          |

See [API Docs](https://docs.qingcloud.com/qingstor/api/object/options.html) for more information about response headers.

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

Then set the input parameters used by the OptionsObject method and perform `options_object` method.
object_key Sets the filepath of the object to be options (in the current bucket).

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

For parameter details, please refer to [Official API Documentation](https://docs.qingcloud.com/qingstor/api/object/options).

The response will return all allowed operations (including header, method, origin) after filtering.
