# Change Log

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).

## [2.5.0] - 2020-11-26

### Added

- bucket: Add replication support(#67)

### Fixed

- build: Fix custom metadata not set correctly (#66)
- request: Fix dict not handled properly in canonicalized headers (#65)

## [2.4.0] - 2020-09-28

### Added

- service: ListBuckets supports limit and offset
- template: Fix CNAME is an abbr
- bucket: Add CNAME support
- bucket: Add logging support
- bucket: Add AppendObject support
- bucket: Add object metadata support

### Changed

- misc: Only python 3 is supported

## [2.3.0] - 2019-05-17

### Added

- service: Add cache-control and content encoding support

### Changed

- sdk/config: Fix yaml loader warning
- misc: Use Pipfile to handle dependence

### Removed

- *: Remove compat for python 2
- client: Remove encryption client support


## [2.2.6] - 2018-07-09

### Added

- Add support for lifecycle and notification

### Fixed

- Fix key error while delete not return content-type

## [2.2.5] - 2017-10-02

### Fixed

- Fix concurrency issue in object related methods

## [2.2.4] - 2017-09-05

### Added

- Add ok property to Unpacker

### Changed

- Force the zone ID to be lowercase

### Fixed

- Fix bug that next not return data
- Fix bug that abort upload shoule return 204

## [2.2.3] - 2017-08-23

### Added

- Add timeout support for sending request
- Add encryption_client class
- Add EncryptionFileChunk class

### Fixed

- Fix bug that response-* params use underline
- Fix bug that response-* params not in sub_resource

## [2.2.2] - 2017-08-16

### Fixed

- Add image and notification into sub resource list

## [2.2.1] - 2017-08-15

### Added

- Add support for x-qs-date header

### Fixed

- Fix x-qs-fetch-source not handled right

## [2.2.0] - 2017-08-14

### Added

- Add images process support
- Add upload client and file chunk classes
- Be compatible with new style classes

### Fixed

- Fix non-ascii data not handled right in Builder
- Fix canonicalized headers not sorted by key

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

[2.5.0]: https://github.com/yunify/qingstor-sdk-python/compare/2.4.0...2.5.0
[2.4.0]: https://github.com/yunify/qingstor-sdk-python/compare/2.3.0...2.4.0
[2.3.0]: https://github.com/yunify/qingstor-sdk-python/compare/2.2.6...2.3.0
[2.2.6]: https://github.com/yunify/qingstor-sdk-python/compare/2.2.5...2.2.6
[2.2.5]: https://github.com/yunify/qingstor-sdk-python/compare/2.2.4...2.2.5
[2.2.4]: https://github.com/yunify/qingstor-sdk-python/compare/2.2.3...2.2.4
[2.2.3]: https://github.com/yunify/qingstor-sdk-python/compare/2.2.2...2.2.3
[2.2.2]: https://github.com/yunify/qingstor-sdk-python/compare/2.2.1...2.2.2
[2.2.1]: https://github.com/yunify/qingstor-sdk-python/compare/2.2.0...2.2.1
[2.2.0]: https://github.com/yunify/qingstor-sdk-python/compare/2.1.3...2.2.0
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
