# Service Initialization

First, we need to initialize a QingStor service to call the services provided by QingStor.

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)

bucket_srv = qingstor.Bucket("your-bucket-name", "zone-name")
```

The object that appears in the above code:
- The `config` object carries the user's authentication information and configuration.
- The `qingstor` object is used to operate the QingStor object storage service, which is used to call all Service level APIs or to create a specified Bucket object to call Bucket and Object level APIs.
- The `bucket_srv` object is bound to the specified bucket and provides a series of object storage operations for the bucket.
