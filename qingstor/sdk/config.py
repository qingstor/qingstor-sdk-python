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

import os
import sys
import yaml
import logging

default_config_file_content = (
    "# QingStor Services Configuration\n"
    "access_key_id: ''\n"
    "secret_access_key: ''\n"
    "host: 'qingstor.com'\n"
    "port: 443\n"
    "protocol: 'https'\n"
    "connection_retries: 3\n"
    "# Valid levels are 'debug', 'info', 'warn', 'error', and 'fatal'.\n"
    "log_level: 'warn'\n")

default_config_file = '~/.qingstor/config.yaml'


class Config:

    def __init__(self, access_key_id='', secret_access_key=''):
        self.load_default_config()
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    def __repr__(self):
        return '<Config %r>' % self.access_key_id

    def set_log_level(self):
        logging.basicConfig(
            format=('[%(asctime)s] %(name)s '
                    '%(funcName)s %(levelname)s:\n'
                    '%(message)s'),
            level=logging.WARNING)
        log_level = {
            'debug': 'DEBUG',
            'info': 'INFO',
            'warn': 'WARNING',
            'error': 'ERROR',
            'fatal': 'CRITICAL'
        }.get(self.log_level, 'WARNING')
        self.logger = logging.getLogger('qingstor-sdk')
        self.logger.setLevel(log_level)

    def get_user_config_file_path(self):
        home = os.environ.get('HOME')
        if sys.platform == 'windows':
            home = os.environ.get('HOMEDRIVE') + os.environ.get('HOMEPATH')
            if home == '':
                home = os.environ.get('USERPROFILE')
        return default_config_file.replace('~', home)

    def install_default_user_config(self):
        user_config_file_path = self.get_user_config_file_path()
        user_dir = os.path.dirname(user_config_file_path)
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        with open(user_config_file_path, 'w') as f:
            f.write(default_config_file_content)
            f.close()

    def load_config_from_data(self, data):
        for (k, v) in data.items():
            setattr(self, k, v)
        self.set_log_level()
        return self

    def load_default_config(self):
        config_data = yaml.load(default_config_file_content)
        self.load_config_from_data(config_data)
        return self

    def load_user_config(self):
        user_config_file_path = self.get_user_config_file_path()
        if not os.path.exists(user_config_file_path):
            self.install_default_user_config()
        self.load_config_from_filepath(user_config_file_path)
        return self

    def load_config_from_filepath(self, filepath):
        with open(filepath, 'r') as f:
            config_data = yaml.load(f)
            self.load_config_from_data(config_data)
            f.close()
