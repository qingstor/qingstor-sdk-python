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

from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .bucket import Bucket
from ..request import Request
from ..unpack import Unpacker


class QingStor:
    """QingStor provides QingStor Service API (API Version 2016-01-06)

    Parameters:
        config (Config): Config that initializes a QingStor service

    Attributes:
        config (Config): Config that initializes a QingStor service
        client (requests.Session): Client that sends requests

    """

    def __init__(self, config):
        self.config = config
        self.client = Session()
        retries = Retry(
            total=self.config.connection_retries,
            backoff_factor=1,
            status_forcelist=[500, 502, 503, 504]
        )
        self.client.mount(
            self.config.protocol + "://", HTTPAdapter(max_retries=retries)
        )

    def list_buckets_request(self, location=""):
        """Build request for list_buckets

        Parameters:
            location (string): Limits results to buckets that in the location

        Returns:
            Request: A Request that not signed.

        See Also:
           https://docs.qingcloud.com/qingstor/api/service/get.html

        """
        operation = {
            "API": "ListBuckets",
            "Method": "GET",
            "URI": "/",
            "Headers": {
                "Host": self.config.host,
                "Location": location,
            },
            "Params": {},
            "Elements": {},
            "Properties": {},
            "Body": None
        }
        self.list_buckets_validate(operation)
        return Request(self.config, operation)

    def list_buckets(self, location=""):
        """Send list_buckets_request

        Parameters:
            location (string): Limits results to buckets that in the location

        Returns:
            Unpacker: Server Response that unpacked.

        See Also:
           https://docs.qingcloud.com/qingstor/api/service/get.html

        """
        req = self.list_buckets_request(location=location)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def list_buckets_validate(op):
        """Validate request input for list_buckets

        Parameters:
            op (dict): operation built by input

        Raises:
            ParameterRequiredError: Parameter required not input.
            ParameterValueNotAllowedError: Parameter has not allowed value.

        """
        pass

    def Bucket(self, bucket_name, zone):
        """Create a Bucket instance will QingStor service

        Parameters:
            bucket_name (str): Bucket's name
            zone (str): Zone's name

        Returns:
            Bucket: A Bucket instance

        """
        properties = {"bucket-name": bucket_name, "zone": zone}
        client = self.client
        return Bucket(self.config, properties, client)
