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

import os
import sys
import yaml
import logging
from urllib.parse import urlparse

default_config_file_content = (
    '# QingStor Services Configuration\n'
    'access_key_id: ""\n'
    'secret_access_key: ""\n'
    'host: "qingstor.com"\n'
    'port: 443\n'
    'protocol: "https"\n'
    'connection_retries: 3\n'
    '# Use 0 for never timeout for request\n'
    'timeout: 0\n'
    '# Valid levels are "debug", "info", "warn", "error", and "fatal".\n'
    'log_level: "warn"\n'
    'enable_virtual_host_style: false\n'
    'enable_dual_stack: false\n'
    'zone: ""\n'
    'endpoint: ""\n'
)

config_items_map = [
    "access_key_id", "secret_access_key", "host", "port",
    "protocol", "connection_retries", "timeout", "log_level",
    "enable_virtual_host_style", "zone", "endpoint"
]

default_config_file = "~/.qingstor/config.yaml"


class Config:

    def __init__(self, access_key_id="", secret_access_key=""):
        self.load_config()
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    def __repr__(self):
        return "<Config %r>" % self.access_key_id

    def set_log_level(self):
        logging.basicConfig(
            format=(
                "[%(asctime)s] %(name)s "
                "%(funcName)s %(levelname)s:\n"
                "%(message)s"
            ),
            level=logging.WARNING
        )
        log_level = {
            "debug": "DEBUG",
            "info": "INFO",
            "warn": "WARNING",
            "error": "ERROR",
            "fatal": "CRITICAL"
        }.get(self.log_level, "WARNING")
        self.logger = logging.getLogger("qingstor-sdk")
        self.logger.setLevel(log_level)

    def get_user_config_file_path(self):
        home = os.environ.get("HOME")
        if sys.platform == "windows":
            home = os.environ.get("HOMEDRIVE") + os.environ.get("HOMEPATH")
            if home == "":
                home = os.environ.get("USERPROFILE")
        return default_config_file.replace("~", home)

    def load_config(self):
        self.load_default_config()
        self.load_user_config()
        self.load_from_env()
        if self.endpoint != "":
            u = urlparse(self.endpoint)
            (self.protocol, self.host, self.port)  = (u.scheme, u.hostname, u.port)
        return self

    def load_config_from_data(self, data):
        for (k, v) in data.items():
            setattr(self, k, v)
        self.set_log_level()
        return self

    def load_default_config(self):
        config_data = yaml.safe_load(default_config_file_content)
        self.load_config_from_data(config_data)
        return self

    def load_user_config(self):
        user_config_file_path = os.environ.get("QINGSTOR_CONFIG_PATH")
        if not user_config_file_path:
            user_config_file_path = self.get_user_config_file_path()
        if os.path.exists(user_config_file_path):
            self.load_config_from_filepath(user_config_file_path)
        return self

    def load_config_from_filepath(self, filepath):
        with open(filepath, "r") as f:
            config_data = yaml.safe_load(f)
            self.load_config_from_data(config_data)
            f.close()
        return self

    def load_from_env(self):
        for item in config_items_map:
            key = f"QINGSTOR_{item.upper()}"
            v = os.environ.get(key)
            if v is not None:
                setattr(self, item, v)
        return self


