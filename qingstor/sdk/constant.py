# +-------------------------------------------------------------------------
# | Copyright (C) 2016 Yunify, Inc.
# +-------------------------------------------------------------------------
# | Licensed under the Apache License, Version 2.0 (the "License");
# | you may not use this work except in compliance with the License.
# | You may obtain a copy of the License in the LICENSE file, or at:
# |
# | http://www.apache.org/licenses/LICENSE-2.0
# |
# | Unless required by applicable law or agreed to in writing, software
# | distributed under the License is distributed on an "AS IS" BASIS,
# | WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# | See the License for the specific language governing permissions and
# | limitations under the License.
# +-------------------------------------------------------------------------
# -*- coding: utf-8 -*-

CHUNK_SIZE = 32 * 1024 * 1024

# Http Status Code
# The request is ok
HTTP_OK = 200
# The uploading part is created in the Qing Console
HTTP_CREATED = 201
HTTP_BAD_REQUEST = 400

# Some constants in upload_client
# Default part size of multipart upload
DEFAULT_PART_SIZE = 64 * 1024 * 1024
# The smallest part size
SMALLEST_PART_SIZE = 4 * 1024 * 1024
# The upper bound limitation of parts' number
# Doc link: https://docs.qingcloud.com/qingstor/api/common/error_code.html
MAX_PARTS = 1000

SEGMENT_SIZE=1024
