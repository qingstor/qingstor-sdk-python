# Installation Guide

**Since v2.3.0, qingstor-sdk-python will only support python 3**

## Install from source code

``` bash
$ git clone https://github.com/yunify/qingstor-sdk-python
$ cd qingstor-sdk-python
$ python setup.py install
```

## Install from pypi

```bash
$ pip install qingstor-sdk
```

Next, just include Qingstor sdk in your application:

```python
from qingstor.sdk.config import Config
from qingstor.sdk.service.bucket import Bucket
from qingstor.sdk.service.qingstor import QingStor
```
