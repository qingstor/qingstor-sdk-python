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

import logging

from .constant import CHUNK_SIZE


class Unpacker(dict):

    def __init__(self, res):
        super(Unpacker, self).__init__()
        self.res = res
        self.status_code = res.status_code
        self.logger = logging.getLogger('qingstor-sdk')
        self.logger.debug('%s: %s' % ('status_code', self.status_code))
        self.unpack_response_body()

    @property
    def headers(self):
        return self.res.headers

    @property
    def content(self):
        return self.res.content

    def unpack_response_body(self):
        header = self.res.headers
        if self.res.ok and header['Content-type'] == 'application/json':
            data = self.res.json()
            if data:
                for (k, v) in data.items():
                    self[k] = v
                    self.logger.debug('%s: %s' % (k, v))

    def iter_content(self, chunk_size=CHUNK_SIZE, decode_unicode=False):
        return self.res.iter_content(chunk_size, decode_unicode)
