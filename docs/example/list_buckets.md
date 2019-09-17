# List Buckets

## Code Snippet

Initialize the Qingstor object with your AccessKeyID and SecretAccessKey.

```python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)
```

Then you can get all your Buckets

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
