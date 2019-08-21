# QingStor Service Usage Guide

Import the QingStor and initialize service with a config, and you are ready to use the initialized service. Service only contains one API, and it is 'list_buckets'.
To use bucket related APIs, you need to initialize a bucket from service using 'Bucket' function.

You can use a specified version of a service by import a service package with a date suffix.

``` python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config
```

### Code Snippet

Initialize the QingStor service with a configuration

``` python
qingstor = QingStor(configuration)
```

List buckets

``` python
output = qingstor.list_buckets()

# Print the HTTP status code.
# Example: 200
print(output.status_code)

# Print the bucket count.
# Example: 5
print(output['count'])

# Print the name of first bucket.
# Example: 'test-bucket'
print(output['buckets'][0]['name'])
```

Initialize a QingStor bucket

``` python
bucket = qingstor.Bucket('test-bucket', 'pek3a')
```

List objects in the bucket

``` python
output = bucket.list_objects()

# Print the HTTP status code.
# Example: 200
print(output.status_code)

# Print the key count.
# Example: 7
print(len(output['keys']))
```

Set ACL of the bucket

``` python
output = bucket.put_acl(acl=[
    {
        'grantee': {
            'type': 'group',
            'name': 'QS_ALL_USERS'
        },
        'permission': 'FULL_CONTROL'
    }
])

# Print the HTTP status code.
# Example: 200
print(output.status_code)
```

Put object

``` python
with open('/tmp/sdk_bin') as f:
    output = bucket.put_object(
        'example_key', body=f
    )

# Print the HTTP status code.
# Example: 201
print(output.status_code)

```

Delete object

``` python
output = bucket.delete_object('example_key')

# Print the HTTP status code.
# Example: 204
print(output.status_code)
```

Initialize Multipart Upload

``` python
output = bucket.initiate_multipart_upload(
	'QingCloudInsight.mov',
	content_type: 'video/quicktime',
)

# Print the HTTP status code.
# Example: 200
print(output.status_code)

# Print the upload ID.
# Example: '9d37dd6ccee643075ca4e597ad65655c'
print(output['upload_id'])
```

Upload Multipart

``` python
with open('/tmp/file0', 'rb') as file0:
    output 
        = bucket.upload_multipart(
            'QingCloudInsight.mov',
            upload_id='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
            part_number=0,
            body=file0,
        )

# Print the HTTP status code.
# Example: 201
print(output.status_code)

with open('/tmp/file1', 'rb') as file1:
    output = bucket.upload_multipart(
        'QingCloudInsight.mov',
        upload_id='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        part_number=1,
        body=file1,
    )

# Print the HTTP status code.
# Example: 201
print(output.status_code)

with open('/tmp/file2', 'rb') as file2:
    output = bucket.upload_multipart(
        'QingCloudInsight.mov',
        upload_id='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        part_number=2,
        body=file2,
    )

# Print the HTTP status code.
# Example: 201
print(output.status_code)
```

Complete Multipart Upload

``` python
output = bucket.complete_multipart_upload(
    'QingCloudInsight.mov',
    upload_id:    'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    object_parts: {
        part_number: 0,
        part_number: 1,
        part_number: 2,
    }
)

# Print the HTTP status code.
# Example: 200
print(output.status_code)
```

Abort Multipart Upload

``` python
output = bucket.abort_multipart_upload(
    'QingCloudInsight.mov',
    upload_id:  'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
)

# Print the error message.
# Example: 400
print(output.status_code)
```

GET Object Download Url Example

1. Initialize the Bucket service with accesskeyid and secretaccesskey.

    ```python
    import time

    from urllib.request import urlretrieve, pathname2url
    from qingstor.sdk.service.qingstor import QingStor
    from qingstor.sdk.config import Config

    config = Config('YOUR_ACCESS_KEY_ID', 'YOUR_SECRET_ACCESS_KEY')
    qingstor = QingStor(config)
    bucket_api = qingstor.Bucket("your-bucket-name", "your-zone-name")
    ```

2. Then you can get object signature url.

    ```python
    # you can get object through the signatured URL：
    testfile = urlretrieve(req.url, "testfile")
    # the url above can also be open with browser. If it is some file type browser could preview, than browser will perform it, otherwise download will be executed.
    ```

3. If you open the url above in the browser, you may see the file preview instead of downloading. To get a url for downloading only, use the method below.

    ```python
    disposition = "attachment; filename=\"test_file\""
    # if chinese character or character need escape is used, you can use function pathname2url to encode it.
    # encoded_filename = pathname2url("测试文件")
    # disposition = "attachment; filename=\"%s\"; filename*=utf-8''%s" % (encoded_filename, encoded_filename)
    # you can open the generated url in browser, the browser will download and save it with specified file name.
    req = bucket_api.get_object_request("logo.svg", response_content_disposition=disposition)
    expire_time = int(time.time()) + 60
    req = req.sign_query(expire_time)
    print(req.url)
    ```
