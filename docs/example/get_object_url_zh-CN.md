# 获取文件的下载地址

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

想要了解详细的参数信息，可以参考[官方 API 文档](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/get/)。

然后你可以获得该对象的签名地址。object_key 设置要获取的对象的 filepath（位于当前 bucket 中）。

```python
import time

# Replace this with some object exists in your bucket
object_key = "your-picture.jpg"
rq = bucket_srv.get_object_request(object_key=object_key)
rq = rq.sign_query(int(time.time()) + 600)
print(rq.url)
```

打印出的 url 是可以直接在浏览器中打开的，如果是浏览器支持预览的格式，浏览器会其进行预览，否则已默认文件名下载保存。
如果您想要设置保存的文件名，直接执行下载动作，可以进行如下设置：

```python
import time
from urllib import parse

# Replace this with some object exists in your bucket
object_key = "your-picture.jpg"
filename = "临时temp.jpg"
encoded_filename = parse.quote(filename)
disposition = "attachment; filename=\"%s\"; filename*=utf-8''%s" % (encoded_filename, encoded_filename)
rq = bucket_srv.get_object_request(object_key=object_key, response_content_disposition=disposition)
rq = rq.sign_query(int(time.time()) + 600)
print(rq.url)
```
