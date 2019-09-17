## 大文件分段上传

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

然后设置 `upload_multipart` 方法用到的输入参数（使用 UploadMultipartInput 存储）。
其中会涉及到 UploadID, PartNumber, ContentLength, Body 几个参数。

首先需要申请一个 UploadID。用于后续在上传分段时，在请求参数中附加该 Upload ID，则表明分段属于同一个对象。objKey 用于指定分段上传完成后的 filepath。

```python
object_key = "your_file_multi_uploaded.zip"
init_resp = bucket_srv.initiate_multipart_upload(object_key=object_key,
                                                      content_type="application/octet-stream")
upload_id = init_resp['upload_id']
print(upload_id)
```

开始分段上传。为了得到分段上传的 part 信息。我们也需要计算 part count 相关信息。

```python
filepath = "/home/max/Pictures/test/your_file_multi_uploaded.zip"
chunk_size = 5 * (1 << 20)  # 5M
file_size = os.stat(filepath).st_size
parts_count = int(math.ceil(file_size / chunk_size))
with open(filepath, 'rb') as f:
    for i in range(parts_count):
        part_size = min(chunk_size, file_size - i * chunk_size)
        data = f.read(part_size)
        part_resp = bucket_srv.upload_multipart(object_key, upload_id=upload_id,
                                                     part_number=str(i), body=data)
        if part_resp.status_code != 201:
            print("Upload part of object(name: {}) to bucket({}) failed with given message: {}".format(
                object_key,
                bucket_name,
                str(part_resp.content, 'utf-8')))
            abort_resp = bucket_srv.abort_multipart_upload(object_key, upload_id)
            print("Abort multi upload executed: 204 expected, actually: %d", abort_resp.status_code)
        else:
            print("Part %d uploaded." % i)
```

查看已上传的分段。可以尝试访问以下方法查看是否所有的分段都已上传完成。它将返回所有的已上传分段信息。

```python
list_resp = bucket_srv.list_multipart(object_key=object_key, upload_id=upload_id)
```

当所有分段都已经上传完毕后，您可以使用下面的方法来标记上传完成，所有分段将拼接为 object_key 指定的对象。
ETag 信息不是必须设置，想要了解详细的参数信息，可以参考 [api docs](https://docs.qingcloud.com/qingstor/api/object/multipart/complete_multipart_upload.html)。

```python
if fin_resp.status_code != 201:
    print("Finish multi-Upload object(name: {}) to bucket({}) failed with given message: {}".format(
        object_key,
        bucket_name,
        str(part_resp.content, 'utf-8')))
    abort_resp = bucket_srv.abort_multipart_upload(object_key, upload_id)
    print("Abort multi upload executed: 204 expected, actually: %d", abort_resp.status_code)
else:
    print("Object uploaded.")
```

如果您想要取消分段上传，只需要指定 object_key 和 uploadID 即可。

```python
abort_resp = bucket_srv.abort_multipart_upload(object_key, upload_id)
print("Abort multi upload executed: 204 expected, actually: %d", abort_resp.status_code)
```
