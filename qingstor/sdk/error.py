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


class ParameterRequiredError(Exception):

    def __init__(self, parameter_name, parent_name):
        self.parameter_name = parameter_name
        self.parent_name = parent_name

    def __str__(self):
        return ''.join(
            [self.parameter_name, ' is required in ', self.parent_name])


class ParameterValueNotAllowedError(Exception):

    def __init__(self, parameter_name, parameter_value, allowed_values):
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.allowed_values = allowed_values

    def __str__(self):
        return ''.join([
            self.parameter_name, ' value ', self.parameter_value,
            ' is not allowed, should be one of ', ', '.join(self.allowed_values)
        ])
