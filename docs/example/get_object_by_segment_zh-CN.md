# 大文件分段下载

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

这里必须手动设置的参数是 Range 参数。想要了解详细的参数信息，可以参考[官方 API 文档](https://docs.qingcloud.com/qingstor/api/object/get)。

然后调用 `get_object` 方法下载对象，将 5M 设置为分段大小。object_key 设置要获取的对象的 filepath（位于当前 bucket 中）。

```python
object_key = "your_zip_fetch_with_seg.zip"
part_size = 1024 * 1024 * 5  # 5M every part.
# ensure the file we will write to does not exists.
if os.path.exists("/tmp/" + object_key):
    os.remove("/tmp/" + object_key)
i = 0
while True:
    lo = part_size * i
    hi = part_size * (i + 1) - 1
    byte_range = "bytes=%d-%d" % (lo, hi)
    output = bucket_srv.get_object(object_key=object_key, range=byte_range)
    if output.status_code != 206:
        print("Get object(name: {}) by segment in bucket({}) failed with given message: {}".format(
            object_key,
            bucket_name,
            str(output.content, 'utf-8')))
        os.remove("/tmp/" + object_key)
        break
    else:
        with open("/tmp/" + object_key, 'a+b') as f:  # append to file in binary mode
            f.write(output.content)
        if len(output.content) < part_size:
            break
        i += 1
```

文件将被保存至 /tmp/{object_key}（请替换为您的 object_key）。
