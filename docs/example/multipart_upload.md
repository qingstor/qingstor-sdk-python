# UploadMultipart Example

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

Then set the input parameters used by the `upload_multipart` method.
Required parameters include UploadID, PartNumber, ContentLength, Body.

First you need to apply for an UploadID. For subsequent uploading of the segment, appending the Upload ID to the request parameter indicates that the segment belongs to the same object. objKey is used to specify the filepath after the segment upload is completed.

```python
object_key = "your_file_multi_uploaded.zip"
init_resp = bucket_srv.initiate_multipart_upload(object_key=object_key,
                                                      content_type="application/octet-stream")
upload_id = init_resp['upload_id']
print(upload_id)
```

Start a multipart upload. In order to get the part information of the segment upload. We also need to calculate part counts info.

```python
import os
import math

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

View the uploaded segments. Try the following methods to see if all the segments have been uploaded. It will return all uploaded segmentation information.

```python
list_resp = bucket_srv.list_multipart(object_key=object_key, upload_id=upload_id)
```

Once all the segments have been uploaded, you can use the following method to mark the upload completion, all segments will be stitched to the object specified by object_key.
ETag header is not required to be set. For parameter details, please refer to [api docs] (https://docs.qingcloud.com/qingstor/api/object/multipart/complete_multipart_upload.html).

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

If you want to cancel a multipart upload, just specify object_key and uploadID.

```python
abort_resp = bucket_srv.abort_multipart_upload(object_key, upload_id)
print("Abort multi upload executed: 204 expected, actually: %d", abort_resp.status_code)
```
