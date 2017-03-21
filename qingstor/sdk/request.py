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

import hmac
import base64
import logging
from hashlib import sha256

from requests.utils import quote, unquote, urlparse, urlunparse
from .build import Builder


class Request:
    """Request which can sign and be sent

    Parameters:
        config (Config): Config that initializes a QingStor service
        operation (dict): operation built by input

    Attributes:
        req (Req): Req built bt Builder
        access_key_id (str): user's access_key_id
        secret_access_key (str): user's secret_access_key
        logger (Logger): qingstor-sdk logger

    """

    def __init__(self, config, operation):
        self.req = Builder(config, operation).parse()
        self.access_key_id = config.access_key_id
        self.secret_access_key = config.secret_access_key
        self.logger = logging.getLogger("qingstor-sdk")

    def __repr__(self):
        return "<Request %s>" % self.req.method

    def sign(self):
        """Sign a request

        Returns:
            requests.PreparedRequest: request that signed and prepared

        """
        self.req.headers["Authorization"] = "".join(
            ["QS ", self.access_key_id, ":", self.get_authorization()]
        )
        self.logger.debug(self.req.headers["Authorization"])
        prepared = self.req.prepare()
        scheme, netloc, path, params, query, fragment = urlparse(
            prepared.url, allow_fragments=False
        )
        path = quote(unquote(path))
        prepared.url = urlunparse(
            (scheme, netloc, path, params, query, fragment)
        )
        return prepared

    def sign_query(self, expires):
        """Sign a request will query_sign

        Parameters:
            expires (int): a unix timestamp that defined when will this query sign expired

        Returns:
            requests.PreparedRequest: request that signed and prepared

        """
        del self.req.headers["Content-Type"]
        prepared = self.req.prepare()
        scheme, netloc, path, params, req_query, fragment = urlparse(
            prepared.url, allow_fragments=False
        )
        path = quote(unquote(path))
        query = [
            req_query, "signature=%s" % self.get_query_signature(expires),
            "access_key_id=%s" % self.access_key_id,
            "expires=%s" % str(expires)
        ]
        if not req_query:
            query.pop(0)
        prepared.url = urlunparse((scheme, netloc, path, params, "", fragment)
                                  ) + "?" + "&".join(query)
        return prepared

    def get_content_md5(self):
        """Get content md5 from header

        Returns:
            str: content md5 from header

        """
        content_md5 = self.req.headers.get("Content-MD5", "")
        return content_md5

    def get_content_type(self):
        """Get content type from header

        Returns:
            str: content type from header

        """
        content_type = self.req.headers.get("Content-Type", "")
        return content_type

    def get_date(self):
        """Get date from header

        Returns:
            str: date from header

        """
        date = self.req.headers.get("Date", "")
        return date

    def get_canonicalized_headers(self):
        """Get canonicalized headers from header

        Returns:
            list: canonicalized headers from header

        """
        headers = self.req.headers
        keys = list()
        for (k, v) in headers.items():
            if k[:5].lower() == "x-qs-":
                keys.append("".join([k.lower().strip(), ":", v.strip()]))
        keys = sorted(keys)
        canonicalized_headers = "\n".join(keys)
        if canonicalized_headers:
            canonicalized_headers += "\n"
        return canonicalized_headers

    def get_canonicalized_resource(self):
        """Get canonicalized resource from header

        Returns:
            str: canonicalized resource from header

        """
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
        if "&".join(keys):
            canonicalized_resource += "?%s" % "&".join(keys)
        self.logger.debug(canonicalized_resource)
        return canonicalized_resource

    def get_authorization(self):
        """Get signature authorization by operation

        Returns:
            str: signature string

        """
        string_to_sign = "".join([
            self.req.method + "\n", self.get_content_md5() + "\n",
            self.get_content_type() + "\n", self.get_date() + "\n",
            self.get_canonicalized_headers(), self.get_canonicalized_resource()
        ])
        self.logger.debug(string_to_sign)
        h = hmac.new(
            self.secret_access_key.encode("utf-8"),
            string_to_sign.encode("utf-8"),
            digestmod=sha256
        )
        signature = base64.b64encode(h.digest()).strip().decode()
        return signature

    def get_query_signature(self, expires):
        """Get query signature authorization by operation

        Returns:
            str: signature string

        """
        string_to_sign = "".join([
            self.req.method + "\n", self.get_content_md5() + "\n", "\n",
            str(expires) + "\n", self.get_canonicalized_headers(),
            self.get_canonicalized_resource()
        ])
        self.logger.debug(string_to_sign)
        h = hmac.new(
            self.secret_access_key.encode("utf-8"),
            string_to_sign.encode("utf-8"),
            digestmod=sha256
        )
        signature = quote(base64.b64encode(h.digest()).strip())
        return signature

    def is_sub_resource(self, key):
        """Judge whether the key is a sub resource

        Parameters:
            key (str): the key need to be judged

        Returns:
            bool: True is the key is a sub resource else False

        """
        keys_map = [
            "acl", "cors", "delete", "mirror", "part_number", "policy", "stats",
            "upload_id", "uploads"
        ]
        return key in keys_map
