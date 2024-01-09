# ListObjects Example

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

then you can list objects

```python
resp = bucket_srv.list_objects()
if resp.status_code != 200:
    print("List objects of bucket({}) failed with given message: {}".format(
        bucket_name,
        str(resp.content, 'utf-8')))
else:
    print(resp['keys'])
```

Add some options which act as filter when list bucket objects

You can set options below in ListObjectsInput. See controlled [API Docs](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/bucket/basic_opt/get/).

| Parameter name |  Type   | Description                                                                                                                                                                                                                                                         | Required |
| :------------: | :-----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------: |
|     prefix     | String  | Limits the response to keys that begin with the specified prefix.                                                                                                                                                                                                   |    No    |
|   delimiter    |  Char   | A delimiter is a character you use to group keys.<br/>If you specify a prefix, all keys that contain the same string between the prefix and the first occurrence of the delimiter after the prefix are grouped under a single result element called CommonPrefixes. |    No    |
|     marker     | String  | Specifies the key to start with when listing objects in a bucket.                                                                                                                                                                                                   |    No    |
|     limit      | Integer | Sets the maximum number of objects returned in the response body. Default is 200, maximum is 1000.                                                                                                                                                                  |    No    |

The following code shows all the objects in the *test* folder in Bucket (without subfolders), sorted by file name by default.

```python
def list_object(bucket_srv: Bucket, prefix: str, marker: str) -> str:
    delimiter = "/"
    limit = 3
    resp = bucket_srv.list_objects(delimiter, str(limit), marker, prefix)
    if resp.status_code != 200:
        print("List objects of bucket({}) failed with given message: {}".format(
            bucket_srv.properties['bucket_name'],
            str(resp.content, 'utf-8')))
    else:
        print("================= List Objects ==================")
        for obj_info in resp['keys']:
            print(obj_info['key'])
        return resp['next_marker']
```

If the return value is not empty, there is still data on the next page, you can continue to access. The following is an example of a call:

```python
next_marker = list_object(bucket_srv, "test/", "")
while next_marker is not None and next_marker != "":
    next_marker = list_object(bucket_srv, "test/", next_marker)
```
