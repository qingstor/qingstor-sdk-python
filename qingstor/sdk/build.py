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

import sys
import json
import base64
import hashlib
import logging
import platform
import mimetypes
from urllib.parse import urlparse, quote, urlunparse

from requests import Request as Req
from requests.structures import CaseInsensitiveDict

from . import __version__
from .constant import BINARY_MIME_TYPE, JSON_MIME_TYPE
from .utils.helper import current_time, url_quote, should_quote, should_url_quote


class Builder:

    def __init__(self, config, operation):
        self.config = config
        self.operation = operation
        self.logger = logging.getLogger("qingstor-sdk")
        self.properties = self.parse_request_properties()

    def __repr__(self):
        return "<Builder>"

    def parse(self):
        parsed_operation = dict()
        parsed_operation["Method"] = self.operation["Method"]
        parsed_operation["URI"] = self.parse_request_uri()
        self.logger.debug(f'parsed_uri: {parsed_operation["URI"]}')
        parsed_body, _ = self.parse_request_body()
        if parsed_body:
            parsed_operation["Body"] = parsed_body
        parsed_headers = self.parse_request_headers()
        if parsed_headers:
            parsed_operation["Headers"] = parsed_headers
        req = Req(
            parsed_operation["Method"],
            parsed_operation["URI"],
            data=parsed_body,
            headers=parsed_headers
        )
        return req

    def parse_request_params(self):
        parsed_params = dict()
        if "Params" in self.operation:
            for (k, v) in self.operation["Params"].items():
                if v != "" and v is not None:
                    parsed_params[k] = quote(v)

        return parsed_params

    def parse_request_headers(self):
        parsed_headers = CaseInsensitiveDict()

        # Parse headers from operation.
        if "Headers" in self.operation:
            for (k, v) in self.operation["Headers"].items():
                k = k.lower()
                if should_quote(k):
                    v = quote(v)
                elif should_url_quote(k):
                    v = url_quote(v)
                parsed_headers[k] = v

        # Handle header Host
        parsed_headers["Host"] = self.parse_request_host()

        # Handle header Date
        parsed_headers["Date"] = self.operation["Headers"].get(
            "Date", current_time()
        )

        # Handle header User-Agent
        parsed_headers["User-Agent"] = (
            "qingstor-sdk-python/{sdk_version}  "
            "(Python v{python_version}; {system})"
        ).format(
            sdk_version=__version__,
            python_version=platform.python_version(),
            system=sys.platform
        )

        # Handle header X-QS-MetaData dict, for example:
        # {'X-QS-MetaData': {'x': 'vx', 'y': 'vy'}} => {'X-QS-Meta-x': 'vx', 'X-QS-Meta-y': 'vy'}
        # https://docs.qingcloud.com/qingstor/api/common/metadata#%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E5%AF%B9%E8%B1%A1%E5%85%83%E6%95%B0%E6%8D%AE
        if 'X-QS-MetaData' in parsed_headers:
            metadata = parsed_headers.get('X-QS-MetaData')
            if isinstance(metadata, dict) and len(metadata) != 0:
                for k, v in parsed_headers['X-QS-MetaData'].items():
                    parsed_headers["X-QS-Meta-{}".format(k)] = v
            del parsed_headers['X-QS-MetaData']

        # Handle header Content-Type
        parsed_body, is_json = self.parse_request_body()
        filename = urlparse(self.parse_request_uri()).path
        parsed_headers["Content-Type"] = self.operation[
            "Headers"].get("Content-Type") or mimetypes.guess_type(filename)[0]
        if is_json:
            parsed_headers["Content-Type"] = JSON_MIME_TYPE
        if parsed_headers["Content-Type"] is None:
            parsed_headers["Content-Type"] = BINARY_MIME_TYPE

        # Handle specific API
        if "API" in self.operation:
            if self.operation["API"] == "DeleteMultipleObjects":
                md5obj = hashlib.md5()
                md5obj.update(parsed_body.encode())
                parsed_headers["Content-MD5"] = base64.b64encode(
                    md5obj.digest()
                ).decode()

        return parsed_headers

    def parse_request_body(self):
        parsed_body = None
        is_json = False
        if "Body" in self.operation and self.operation["Body"]:
            parsed_body = self.operation["Body"]
        elif "Elements" in self.operation and self.operation["Elements"]:
            parsed_body = json.dumps(self.operation["Elements"], sort_keys=True)
            is_json = True

        return parsed_body, is_json

    def parse_request_properties(self):
        parsed_properties = dict()
        for (k, v) in self.operation["Properties"].items():
            if v != "" and v is not None:
                parsed_properties[k] = quote(v)

        return parsed_properties

    def parse_request_host(self):
        zone = self.properties.get("zone", "")
        bucket_name = self.properties.get("bucket-name", "")

        (protocol, endpoint,
         port) = (self.config.protocol, self.config.host, self.config.port)

        # Omit port if https:443 or http:80
        if not ((protocol == "https" and port == 443) or
                (protocol == "http" and port == 80)):
            endpoint = f"{endpoint}:{port}"
        if zone != "":
            endpoint = f"{zone}.{endpoint}"
        if bucket_name != "" and self.config.enable_virtual_host_style:
            endpoint = f"{bucket_name}.{endpoint}"

        return endpoint

    def parse_request_uri(self):
        request_uri = self.operation["URI"]
        if self.config.enable_virtual_host_style and request_uri.startswith(
                "/<bucket-name>"):
            request_uri = request_uri.replace("/<bucket-name>", "")

        if len(self.properties):
            for (k, v) in self.properties.items():
                request_uri = request_uri.replace("<%s>" % k, v)

        parsed_uri = f"{self.config.protocol}://{self.parse_request_host()}{request_uri}"
        parsed_params = self.parse_request_params()
        if len(parsed_params):
            scheme, netloc, path, params, req_query, fragment = urlparse(
                parsed_uri, allow_fragments=False
            )
            query = [req_query]
            for (k, v) in parsed_params.items():
                query.append("%s=%s" % (k, v))
            if not req_query:
                query.pop(0)
            parsed_uri = urlunparse(
                (scheme, netloc, path, params, "", fragment)
            ) + "?" + "&".join(sorted(query))
        return parsed_uri
