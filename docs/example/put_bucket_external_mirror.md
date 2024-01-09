# PUT Bucket External Mirror

## Request Elements

|    Name     |  Type  | Description                                                                                                                                                                                                                                                                                                                                                                          | Required |
| :---------: | :----: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: |
| source_site | String | Source site of external mirror source. Source site is like this: `<protocol>://<host>[:port]/[path]` . Valid values of protocol: “http” or “https”, default “http”. Port defaults to the port corresponding to the protocol. Path can be empty. If the storage space has multiple source sites for many times, the source site of the storage space will use the last setting value. |   Yes    |

See [API Docs](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/bucket/external_mirror/put_external_mirror/) for more information about request elements.

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

then you can PUT Bucket External Mirror

```python
source_site = "http://example.com:80/image/"
resp = bucket_srv.put_external_mirror(source_site=source_site)
if resp.status_code != 200:
    print("Set external mirror of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name, str(resp.content, "utf-8")))
else:
    print("Put bucket external mirror successfully.")
```
