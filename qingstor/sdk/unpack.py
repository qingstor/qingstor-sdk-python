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

from __future__ import unicode_literals

import logging

from .constant import CHUNK_SIZE


class Unpacker(dict):
    """Unpack a request.Response for user

    Parameters:
        res (request.Response): a request.Response from server

    Attributes:
        res (request.Response): a request.Response from server
        status_code (int): the response's status_code
        logger (Logger): qingstor-sdk logger

    """
    def __init__(self, res):
        super(Unpacker, self).__init__()
        self.res = res
        self.status_code = res.status_code
        self.logger = logging.getLogger("qingstor-sdk")
        self.logger.debug("%s: %s" % ("status_code", self.status_code))
        self.unpack_response_body()

    @property
    def headers(self):
        """dict: the response's headers"""
        return self.res.headers

    @property
    def content(self):
        """str: the response's content"""
        return self.res.content

    def unpack_response_body(self):
        """Unpack the response's body

        Raises:
            ValueError: If the data should by json but it's empty

        """
        try:
            data = self.res.json()
        except ValueError:
            data = None
        if data:
            for (k, v) in data.items():
                self[k] = v
                self.logger.debug("%s: %s" % (k, v))


    def iter_content(self, chunk_size=CHUNK_SIZE, decode_unicode=False):
        """iter the content with chunk_size

        Parameters:
            chunk_size (int): the chunk size used in every iter
            decode_unicode (bool): decode unicode or not

        Yields:
            str: The next chunk from content

        """
        return self.res.iter_content(chunk_size, decode_unicode)
