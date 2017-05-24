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

import sys
import json
import base64
import hashlib
import logging
import platform
import mimetypes
from time import strftime, gmtime

from requests import Request as Req
from requests.utils import quote, urlparse, urlunparse

from . import __version__
from .compat import is_python2, is_python3


class Builder:

    def __init__(self, config, operation):
        self.config = config
        self.operation = operation
        self.logger = logging.getLogger("qingstor-sdk")

    def __repr__(self):
        return "<Builder>"

    def parse(self):
        parsed_operation = dict()
        parsed_operation["Method"] = self.operation["Method"]
        parsed_operation["URI"] = self.parse_request_uri()
        self.logger.debug("parsed_uri: %s" % parsed_operation["URI"])
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
                    if is_python2:
                        parsed_params[k] = quote(unicode(v).encode("utf-8"))
                    elif is_python3:
                        parsed_params[k] = quote(str(v))

        return parsed_params

    def parse_request_headers(self):
        parsed_headers = dict()
        if "Headers" in self.operation:
            for (k, v) in self.operation["Headers"].items():
                if v != "" and v is not None:
                    if k[:5].lower() == "x-qs-":
                        k = k.lower()
                        if is_python2:
                            parsed_headers[k] = quote(
                                unicode(v).encode("utf-8")
                            )
                        elif is_python3:
                            parsed_headers[k] = quote(str(v))
                    else:
                        parsed_headers[k] = v

            # Handle header Date
            if is_python2:
                parsed_headers["Date"] = self.operation["Headers"].get(
                    "Date",
                    strftime(
                        "%a, %d %b %Y %H:%M:%S GMT".encode("utf-8"), gmtime()
                    )
                )
            elif is_python3:
                parsed_headers["Date"] = self.operation["Headers"].get(
                    "Date", strftime("%a, %d %b %Y %H:%M:%S GMT", gmtime())
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

            # Handle header Content-Type
            parsed_body, is_json = self.parse_request_body()
            filename = urlparse(self.parse_request_uri()).path
            parsed_headers["Content-Type"] = self.operation["Headers"].get(
                "Content-Type"
            ) or mimetypes.guess_type(filename)[0]
            if is_json:
                parsed_headers["Content-Type"] = "application/json"
            if parsed_headers["Content-Type"] is None:
                parsed_headers["Content-Type"] = "application/octet-stream"

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
        if "Properties" in self.operation:
            for (k, v) in self.operation["Properties"].items():
                if v != "" and v is not None:
                    if is_python2:
                        parsed_properties[k] = quote(unicode(v).encode("utf-8"))
                    elif is_python3:
                        parsed_properties[k] = quote(str(v))

        return parsed_properties

    def parse_request_uri(self):
        properties = self.parse_request_properties()
        zone = properties.get("zone", "")
        port = str(self.config.port)
        endpoint = "".join([
            self.config.protocol, "://", self.config.host, ":", port
        ])
        if zone != "":
            endpoint = "".join([
                self.config.protocol, "://", zone, ".", self.config.host, ":",
                port
            ])
        request_uri = self.operation["URI"]
        if len(properties):
            for (k, v) in properties.items():
                endpoint = endpoint.replace("<%s>" % k, v)
                request_uri = request_uri.replace("<%s>" % k, v)
        parsed_uri = endpoint + request_uri
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
