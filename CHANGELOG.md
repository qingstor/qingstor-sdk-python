# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## [2.1.3] - 2017-08-10

### Fixed

- Fix bug that can cause large memory usage
- Fix setup error for python2.6

### Changed

- Requests do not bundle urllib3 any more

## [2.1.2] - 2017-05-24

### Fixed

- Fix load_config_from_filepath not return self
- Fix 40x and 50x response not handle right
- Fix SSL Warnings with old python versions
- Fix request query not sorted
- Fix url query not handled correctly bug
- Fix resource is not mandatory in policy statement

## [2.1.1] - 2017-02-28

### Fixed

- Fix query_sign wrong with content_type
- Fix sign_error generate url error with empty query
- Fix body unpack error with empty body

## [2.1.0] - 2017-02-24

### Added

- Add list multipart uploads API

### Fixed

- Fix request uri not quote correctly
- Fix REAEME.md missing error

## [2.0.3] - 2017-01-21

### Fixed

- Fix wrong quote in headers

## [2.0.2] - 2017-01-17

### Changed

- Use unicode for all input and output

### Fixed

- Fix non-ascii in headers behavior

## [2.0.1] - 2017-01-15

### Fixed

- Fix extra output in request
- Fix bugs in non-ascii characters build in params

## [2.0.0] - 2017-01-12

### Fixed

- Fix compatibility issues on python2

## [2.0.0b5] - 2017-01-09

### Fixed

- Fix bug in content_type detect

## [2.0.0b4] - 2017-01-06

### Fixed

- Fix bug when get content_type

## [2.0.0b3] - 2017-01-04

### Changed

- Builder will check value if exists before use

## [2.0.0b2] - 2017-01-03

### Fixed

- Fix import error

## 2.0.0b1 - 2017-01-03

### Added

- Provide Official Qingstor SDK for Python

[2.1.3]: https://github.com/yunify/qingstor-sdk-python/compare/2.1.2...2.1.3
[2.1.2]: https://github.com/yunify/qingstor-sdk-python/compare/2.1.1...2.1.2
[2.1.1]: https://github.com/yunify/qingstor-sdk-python/compare/2.1.0...2.1.1
[2.1.0]: https://github.com/yunify/qingstor-sdk-python/compare/2.0.3...2.1.0
[2.0.3]: https://github.com/yunify/qingstor-sdk-python/compare/2.0.2...2.0.3
[2.0.2]: https://github.com/yunify/qingstor-sdk-python/compare/2.0.1...2.0.2
[2.0.1]: https://github.com/yunify/qingstor-sdk-python/compare/2.0.0...2.0.1
[2.0.0]: https://github.com/yunify/qingstor-sdk-python/compare/2.0.0b5...2.0.0
[2.0.0b5]: https://github.com/yunify/qingstor-sdk-python/compare/2.0.0b4...2.0.0b5
[2.0.0b4]: https://github.com/yunify/qingstor-sdk-python/compare/2.0.0b3...2.0.0b4
[2.0.0b3]: https://github.com/yunify/qingstor-sdk-python/compare/2.0.0b2...2.0.0b3
[2.0.0b2]: https://github.com/yunify/qingstor-sdk-python/compare/2.0.0b1...2.0.0b2
