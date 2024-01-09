# 列取对象

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

然后您可以得到 Bucket 中的所有对象的记录

```python
resp = bucket_srv.list_objects()
if resp.status_code != 200:
    print("List objects of bucket({}) failed with given message: {}".format(
        bucket_name,
        str(resp.content, 'utf-8')))
else:
    print(resp['keys'])
```

还可以在 List Bucket Objects 时添加筛选条件

参考[对应的 API 文档](https://docsv4.qingcloud.com/user_guide/storage/object_storage/api/bucket/basic_opt/get/)，您可以在对应的 Input 设置并添加如下筛选条件：

|   参数名称    |   类型    |                                   描述                                    | 是否必须 |
|:---------:|:-------:|:-----------------------------------------------------------------------:|:----:|
|  prefix   | String  |                    限定返回的 object key 必须以 prefix 作为前缀                     |  否   |
| delimiter |  Char   | 是一个用于对 Object 名字进行分组的字符。所有名字包含指定的前缀且第一次出现 delimiter 字符之间的 object 作为一组元素 |  否   |
|  marker   | String  |                      设定结果从 marker 之后按字母排序的第一个开始返回                       |  否   |
|   limit   | Integer |                限定此次返回 object 的最大数量，默认值为 200，最大允许设置 1000                 |  否   |

以下代码是展示 Bucket 内 *test* 文件夹的所有对象（不包含子文件夹），默认以文件名排序。

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

如返回值不为空，说明还有下一页数据，可以继续访问。下面是一个调用示例：

```python
next_marker = list_object(bucket_srv, "test/", "")
while next_marker is not None and next_marker != "":
    next_marker = list_object(bucket_srv, "test/", next_marker)
```
