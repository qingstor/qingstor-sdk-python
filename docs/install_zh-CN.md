# 安装指引

**Since v2.3.0, qingstor-sdk-python will only support python 3**

## 从源码安装

``` bash
$ git clone https://github.com/yunify/qingstor-sdk-python
$ cd qingstor-sdk-python
$ python setup.py install
```

## 从 pypi 安装

```bash
$ pip install qingstor-sdk
```

下一步，您只需要将 Qingstor sdk import 到您的项目中即可:

```python
from qingstor.sdk.config import Config
from qingstor.sdk.service.bucket import Bucket
from qingstor.sdk.service.qingstor import QingStor
```
