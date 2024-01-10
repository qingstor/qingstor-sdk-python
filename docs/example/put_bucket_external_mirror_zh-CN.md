# PUT Bucket External Mirror

## 请求消息体

|    名称     |  类型  | 描述                                                                                                                                                                                                                                           | 是否必要 |
| :---------: | :----: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------: |
| source_site | String | 外部镜像回源的源站。源站形式为 `<protocol>://<host>[:port]/[path]` 。 protocol的值可为 “http” 或 “https”，默认为 “http”。port 默认为 protocol 对应的端口。path 可为空。 如果存储空间多次设置不同的源站，该存储空间的源站采用最后一次设置的值。 |   Yes    |

访问 [API Docs](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/bucket/external_mirror/put_external_mirror/) 以查看更多关于请求消息体的信息。

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

然后您可以 PUT Bucket External Mirror

```python
source_site = "http://example.com:80/image/"
resp = bucket_srv.put_external_mirror(source_site=source_site)
if resp.status_code != 200:
    print("Set external mirror of bucket(name: %s) failed with given message: %s\n" % (
        bucket_name, str(resp.content, "utf-8")))
else:
    print("Put bucket external mirror successfully.")
```
