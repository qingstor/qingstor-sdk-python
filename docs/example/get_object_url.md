# GET Object Download Url Example

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

For parameter details, please refer to [Official API Documentation](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/object/basic_opt/get/).

Then you can get the signature address of the object. object_key Sets the filepath of the object to be fetched (in the current bucket).

```python
import time

# Replace this with some object exists in your bucket
filename = "临时temp.jpg"
rq = bucket_srv.get_object_request(object_key=filename)
rq = rq.sign_query(int(time.time()) + 600)
print(rq.url)
```

The printed url can be opened directly in the browser. If the browser supports the preview format, the browser will preview it, otherwise it will be downloaded and saved with the default file name.
If you want to set the saved file name and execute the download directly, you can set as the following code:

```python
import time
from urllib import parse

# Replace this with some object exists in your bucket
filename = "临时temp.jpg"
encoded_filename = parse.quote(filename)
disposition = "attachment; filename=\"%s\"; filename*=utf-8''%s" % (encoded_filename, encoded_filename)
rq = bucket_srv.get_object_request(object_key=filename, response_content_disposition=disposition)
rq = rq.sign_query(int(time.time()) + 600)
print(rq.url)
```
