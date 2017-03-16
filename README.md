# QingStor SDK for Python

[![Build Status](https://travis-ci.org/yunify/qingstor-sdk-python.svg?branch=master)](https://travis-ci.org/yunify/qingstor-sdk-python)
[![API Reference](http://img.shields.io/badge/api-reference-green.svg)](https://docs.qingcloud.com/qingstor/)
[![License](http://img.shields.io/badge/license-apache%20v2-blue.svg)](https://github.com/yunify/qingstor-sdk-python/blob/master/LICENSE)

The official QingStor SDK for the Python programming language.

## Getting Started

### Installation

Refer to the [Installation Guide](docs/installation.md), and have this SDK installed.

### Preparation

Before your start, please python to [QingCloud Console](https://console.qingcloud.com/access_keys/) to create a pair of QingCloud API AccessKey.

___API AccessKey Example:___

``` yaml
access_key_id: 'ACCESS_KEY_ID_EXAMPLE'
secret_access_key: 'SECRET_ACCESS_KEY_EXAMPLE'
```

### Usage

Now you are ready to code. You can read the detailed guides in the list below to have a clear understanding or just take the quick start code example.

Checkout our [releases](https://github.com/yunify/qingstor-sdk-python/releases) and [change log](https://github.com/yunify/qingstor-sdk-python/blob/master/CHANGELOG.md) for information about the latest features, bug fixes and new ideas.

- [Configuration Guide](docs/configuration.md)
- [QingStor Service Usage Guide](docs/qingstor_service_usage.md)

___Quick Start Code Example:___

``` python
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.config import Config

config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
qingstor = QingStor(config)

# List all buckets.
output = qingstor.list_buckets()

# Print HTTP status code.
print(output.status_code)

# Print the count of buckets.
print(output['count'])

# Print the first bucket name.
print(output['buckets'][0]['name'])

# Print Content-Type header.
print(output.headers['Content-Type'])

# Print whole content.
print(output.content)
```

## Reference Documentations

- [QingStor Documentation](https://docs.qingcloud.com/qingstor/index.html)
- [QingStor Guide](https://docs.qingcloud.com/qingstor/guide/index.html)
- [QingStor APIs](https://docs.qingcloud.com/qingstor/api/index.html)

## Contributing

1. Fork it ( https://github.com/yunify/qingstor-sdk-python/fork )
2. Create your feature branch (`git checkout -b new-feature`)
3. Commit your changes (`git commit -asm 'Add some feature'`)
4. Push to the branch (`git push origin new-feature`)
5. Create a new Pull Request

## LICENSE

The Apache License (Version 2.0, January 2004).
