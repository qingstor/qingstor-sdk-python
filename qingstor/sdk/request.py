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

import hmac
import base64
import logging
from hashlib import sha256
from urllib.parse import urlparse, quote, urlunparse, unquote

from .build import Builder
from .utils.helper import url_quote
import requests.packages.urllib3.util.connection as urllib3_cn
import socket


class Request:

    def __init__(self, config, operation):
        self.builder = Builder(config, operation)
        self.req = self.builder.parse()
        self.access_key_id = config.access_key_id
        self.secret_access_key = config.secret_access_key
        self.logger = logging.getLogger("qingstor-sdk")
        self.enable_virtual_host_style = config.enable_virtual_host_style
        urllib3_cn.allowed_gai_family = rewrite_allowed_gai_family(
            config.enable_dual_stack, self.req.headers["Host"]
        )

    def __repr__(self):
        return "<Request %s>" % self.req.method

    def sign(self):
        self.req.headers[
            "Authorization"
        ] = f'QS {self.access_key_id}:{self.get_authorization()}'
        self.logger.debug(self.req.headers["Authorization"])
        prepared = self.req.prepare()
        prepared.url = url_quote(prepared.url)
        return prepared

    def sign_query(self, expires):
        del self.req.headers["Content-Type"]
        prepared = self.req.prepare()
        scheme, netloc, path, params, req_query, fragment = urlparse(
            prepared.url, allow_fragments=False
        )
        path = quote(unquote(path))
        query = [
            req_query,
            "signature=%s" % self.get_query_signature(expires),
            "access_key_id=%s" % self.access_key_id,
            "expires=%s" % str(expires)
        ]
        if not req_query:
            query.pop(0)
        prepared.url = urlunparse((scheme, netloc, path, params, "", fragment)
                                  ) + "?" + "&".join(query)
        return prepared

    def get_content_md5(self):
        return self.req.headers.get("Content-MD5", "")

    def get_content_type(self):
        return self.req.headers.get("Content-Type", "")

    def get_date(self):
        # if user input has x_qs_date, empty Date header is returned.
        if self.req.headers.get("x-qs-date", ""):
            return ""
        date = self.req.headers.get("Date", "")
        return date

    def get_canonicalized_headers(self):
        headers = self.req.headers
        keys = list()
        for k in headers.keys():
            if k[:5].lower() == "x-qs-":
                keys.append(k.lower().strip())
        keys = sorted(keys)
        canonicalized_headers = "\n".join([
            k + ":" + headers[k].strip() for k in keys
        ])
        if canonicalized_headers:
            canonicalized_headers += "\n"
        return canonicalized_headers

    def get_canonicalized_resource(self):
        parsed_uri = urlparse(self.req.url, allow_fragments=False)
        path, query = parsed_uri.path, parsed_uri.query
        keys = list()
        if query:
            for i in query.split("&"):
                if self.is_sub_resource(i.split("=")[0]):
                    if len(i.split("=")) > 1:
                        k, v = i.split("=")
                        keys.append("%s=%s" % (k, v))
                    else:
                        keys.append(i)
            keys = sorted(keys)

        canonicalized_resource = path
        if self.enable_virtual_host_style:
            bucket_name = self.builder.properties.get("bucket-name", "")
            if bucket_name != "":
                # FIXME: Workaround for gateway bug, should be removed after fix.
                if path != "":
                    canonicalized_resource = f"/{bucket_name}{path}"
                else:
                    canonicalized_resource = f"/{bucket_name}/"

        if "&".join(keys):
            canonicalized_resource += "?%s" % "&".join(keys)
        self.logger.debug(canonicalized_resource)
        return canonicalized_resource

    def get_string_to_sign(self, query=False, expires=None):
        sign_parts = [
            self.req.method + "\n",
            self.get_content_md5() + "\n",
            self.get_content_type() + "\n",
            self.get_date() + "\n",
            self.get_canonicalized_headers(),
            self.get_canonicalized_resource()
        ]

        # if query sign is used:
        # - Date should be replaced by expires
        # - Content-Type should be removed
        if query:
            sign_parts[2] = "\n"
            sign_parts[3] = str(expires) + "\n"

        string_to_sign = "".join(sign_parts)
        self.logger.debug(string_to_sign)

        return string_to_sign

    def get_authorization(self):
        string_to_sign = self.get_string_to_sign()
        self.logger.debug(string_to_sign)
        h = hmac.new(
            self.secret_access_key.encode("utf-8"),
            string_to_sign.encode("utf-8"),
            digestmod=sha256
        )
        signature = base64.b64encode(h.digest()).strip().decode()
        return signature

    def get_query_signature(self, expires):
        string_to_sign = self.get_string_to_sign(query=True, expires=expires)
        self.logger.debug(string_to_sign)
        h = hmac.new(
            self.secret_access_key.encode("utf-8"),
            string_to_sign.encode("utf-8"),
            digestmod=sha256
        )
        signature = quote(base64.b64encode(h.digest()).strip())
        return signature

    def is_sub_resource(self, key):
        keys_map = [
            "acl", "cors", "delete", "mirror", "part_number", "policy", "stats",
            "upload_id", "uploads", "image", "notification", "response-expires",
            "response-cache-control", "response-content-type",
            "response-content-language", "response-content-encoding",
            "response-content-disposition", "lifecycle", "logging",
            "replication", "append", "position", "cname"
        ]
        return key in keys_map


def has_ipv6(host):
    """ Returns True if the system resolves host to an IPv6 address by default. """
    resolves_to_ipv6 = False
    try:
        for res in socket.getaddrinfo(host, None, socket.AF_UNSPEC):
            af, _, _, _, _ = res
            if af == socket.AF_INET6:
                resolves_to_ipv6 = True
    except socket.gaierror:
        pass
    return resolves_to_ipv6


def rewrite_allowed_gai_family(use_ipv6, host):
    """ This function is designed to control the choice of address family. """
    def allowed_gai_family():
        family = socket.AF_INET
        if has_ipv6(host):
            if use_ipv6:
                family = socket.AF_INET6
            else:
                family = socket.AF_UNSPEC
        return family
    return allowed_gai_family
