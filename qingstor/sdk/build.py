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

import sys
import json
import base64
import hashlib
import logging
import platform
import mimetypes
from time import strftime, gmtime

from requests import Request as Req
from requests.utils import urlparse

from . import __version__


class Builder:

    def __init__(self, config, operation):
        self.config = config
        self.operation = operation
        self.logger = logging.getLogger('qingstor-sdk')

    def __repr__(self):
        return '<Builder>'

    def parse(self):
        parsed_operation = dict()
        parsed_operation['Method'] = self.operation['Method']
        parsed_operation['URI'] = self.parse_request_uri()
        self.logger.debug('parsed_uri: %s' % parsed_operation['URI'])
        parsed_body = self.parse_request_body()
        if parsed_body:
            parsed_operation['Body'] = parsed_body
        parsed_headers = self.parse_request_headers()
        if parsed_headers:
            parsed_operation['Headers'] = parsed_headers
        req = Req(parsed_operation['Method'],
                  parsed_operation['URI'],
                  data=parsed_body,
                  headers=parsed_headers)
        return req

    def parse_request_params(self):
        parsed_params = dict()
        for (k, v) in self.operation['Params'].items():
            if v != '' and v != {} and v is not None:
                parsed_params[k] = v
        return parsed_params

    def parse_request_headers(self):
        parsed_headers = dict()
        for (k, v) in self.operation['Headers'].items():
            if v != '' and v != {} and v is not None:
                parsed_headers[k] = v
        parsed_headers['Date'] = self.operation['Headers'].get(
            'Date', strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime()))
        parsed_headers['User-Agent'] = (
            'qingstor-sdk-python/{sdk_version}  '
            '(Python v{python_version}; {system})').format(
                sdk_version=__version__,
                python_version=platform.python_version(),
                system=sys.platform)
        parsed_body = self.parse_request_body()
        if parsed_body:
            parsed_headers['Content-Type'] = self.operation['Headers'].get(
                'Content-Type',
                mimetypes.guess_type(urlparse(self.parse_request_uri()).path)[
                    0])
            if parsed_headers['Content-Type'] is None:
                parsed_headers['Content-Type'] = 'application/octet-stream'
        if self.operation['API'] == 'DeleteMultipleObjects':
            md5obj = hashlib.md5()
            md5obj.update(parsed_body.encode())
            parsed_headers['Content-MD5'] = base64.b64encode(md5obj.digest(
            )).decode()

        return parsed_headers

    def parse_request_body(self):
        parsed_body = None
        if self.operation['Body']:
            parsed_body = self.operation['Body']
        elif self.operation['Elements']:
            parsed_body = json.dumps(self.operation['Elements'], sort_keys=True)
        return parsed_body

    def parse_request_properties(self):
        parsed_properties = dict()
        for (k, v) in self.operation['Properties'].items():
            if v != '' and v != {} and v is not None:
                parsed_properties[k] = v
        return parsed_properties

    def parse_request_uri(self):
        properties = self.parse_request_properties()
        zone = properties.get('zone', '')
        port = str(self.config.port)
        endpoint = ''.join(
            [self.config.protocol, '://', self.config.host, ':', port])
        if zone != '':
            endpoint = ''.join([
                self.config.protocol, '://', zone, '.', self.config.host, ':',
                port
            ])
        request_uri = self.operation['URI']
        if len(properties):
            for (k, v) in properties.items():
                endpoint = endpoint.replace('<%s>' % k, v)
                request_uri = request_uri.replace('<%s>' % k, v)
        parsed_uri = endpoint + request_uri

        parsed_params = self.parse_request_params()
        if len(parsed_params):
            params_parts = list()
            for (k, v) in parsed_params.items():
                params_parts.append('%s=%s' % (k, v))
            params_parts = sorted(params_parts)
            joined = '&'.join(params_parts)
            if joined:
                parsed_uri += '?' + joined
        return parsed_uri
