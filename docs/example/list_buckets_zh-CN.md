# 列取 Buckets

## 代码片段

使用您的 AccessKeyID 和 SecretAccessKey 初始化 Qingstor 对象。

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)
```

然后您可以获取您所有的 Buckets

```python
zone = "pek3b"
resp = qingstor.list_buckets(location=zone)
if resp.status_code != 200:
    print("List buckets in zone:{} failed with given message: {}".format(
        zone,
        str(resp.content, 'utf-8')))
else:
    print(resp['buckets'])
```
