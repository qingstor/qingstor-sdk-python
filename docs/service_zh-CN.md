# 初始化服务

首先我们需要初始化一个 QingStor Service 来调用 QingStor 提供的各项服务。

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)

bucket_srv = qingstor.Bucket("your-bucket-name", "zone-name")
```

上面代码中出现的对象：
- `config` 对象承载了用户的认证信息及配置。
- `qingstor` 对象用于操作 QingStor 对象存储服务，用于调用所有 Service 级别的 API 或创建指定的 Bucket 对象来调用 Bucket 和 Object 级别的 API。
- `bucket_srv` 对象绑定了指定 bucket，提供一系列针对该 bucket 的对象存储操作。
