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

import hmac
import base64
import logging
from hashlib import sha256

from requests.utils import quote
from requests.utils import urlparse
from requests.utils import urlunparse

from .build import Builder


class Request:

    def __init__(self, config, operation):
        self.req = Builder(config, operation).parse()
        self.access_key_id = config.access_key_id
        self.secret_access_key = config.secret_access_key
        self.logger = logging.getLogger('qingstor-sdk')

    def __repr__(self):
        return '<Request %s>' % self.req.method

    def sign(self):
        self.req.headers['Authorization'] = ''.join(
            ['QS ', self.access_key_id, ':', self.get_authorization()])
        return self.req.prepare()

    def sign_query(self, expires):
        parsed_uri = urlparse(self.req.url)
        scheme, netloc, path, params, query, fragment = parsed_uri
        query = '&'.join([
            query, 'signature=%s' % self.get_query_signature(expires),
            'access_key_id=%s' % self.access_key_id, 'expires=%s' % str(expires)
        ])
        logging.debug(query)
        self.req.url = urlunparse(
            (scheme, netloc, path, params, query, fragment))
        return self.req.prepare()

    def get_content_md5(self):
        content_md5 = self.req.headers.get('Content-MD5', '')
        return content_md5

    def get_content_type(self):
        content_type = self.req.headers.get('Content-Type', '')
        return content_type

    def get_date(self):
        date = self.req.headers.get('Date', '')
        return date

    def get_canonicalized_headers(self):
        headers = self.req.headers
        keys = list()
        for (k, v) in headers.items():
            if k[:5].lower() == 'x-qs-':
                keys.append(''.join([k.lower().strip(), ':', v.strip()]))
        keys = sorted(keys)
        canonicalized_headers = '\n'.join(keys)
        if canonicalized_headers:
            canonicalized_headers += '\n'
        return canonicalized_headers

    def get_canonicalized_resource(self):
        parsed_uri = urlparse(self.req.url)
        path, query = parsed_uri.path, parsed_uri.query
        keys = list()
        if query:
            for i in query.split('&'):
                if self.is_sub_resource(i.split('=')[0]):
                    if len(i.split('=')) > 1:
                        k, v = i.split('=')
                        keys.append('%s=%s' % (k, quote(v, safe='')))
                    else:
                        keys.append(i)
            keys = sorted(keys)
        canonicalized_resource = path
        if '&'.join(keys):
            canonicalized_resource += '?%s' % '&'.join(keys)
        return canonicalized_resource

    def get_authorization(self):
        string_to_sign = ''.join([
            self.req.method + '\n', self.get_content_md5() + '\n',
            self.get_content_type() + '\n', self.get_date() + '\n',
            self.get_canonicalized_headers(), self.get_canonicalized_resource()
        ])
        self.logger.debug(string_to_sign)
        h = hmac.new(self.secret_access_key.encode(), digestmod=sha256)
        h.update(string_to_sign.encode())
        signature = base64.b64encode(h.digest()).strip().decode()
        return signature

    def get_query_signature(self, expires):
        string_to_sign = ''.join([
            self.req.method + '\n', self.get_content_md5() + '\n',
            self.get_content_type() + '\n', str(expires) + '\n',
            self.get_canonicalized_headers(), self.get_canonicalized_resource()
        ])
        self.logger.debug(string_to_sign)
        h = hmac.new(self.secret_access_key.encode(), digestmod=sha256)
        h.update(string_to_sign.encode())
        signature = quote(base64.b64encode(h.digest()).strip(), safe='')
        return signature

    def is_sub_resource(self, key):
        keys_map = [
            'acl', 'cors', 'delete', 'mirror', 'part_number', 'policy', 'stats',
            'upload_id', 'uploads'
        ]
        return key in keys_map
