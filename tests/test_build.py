import json
import platform
import sys
import unittest

from qingstor.sdk import __version__
from qingstor.sdk.config import Config
from qingstor.sdk.build import Builder


class BuildTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_config = Config('ACCESS_KEY_ID', 'SECRET_ACCESS_KEY')
        cls.test_operation = {
            'API': 'Test',
            'Method': 'GET',
            'URI': '/<bucket-name>/<object-key>',
            'Headers': {
                'Host': 'pek3a.qingstor.com',
                'Date': 'Wed, 10 Dec 2014 17:20:31 GMT',
                'test_empty_header': '',
            },
            'Params': {
                'test_params_1': 'test_val',
                'test_params_2': 'test_val',
                'test_params_empty': '',
            },
            'Elements': {
                'test_elements_1': 'test_val',
                'test_elements_2': 'test_val',
                'test_elements_empty': '',
            },
            'Properties': {
                'zone': 'pek3a',
                'bucket-name': 'test_bucket',
                'object-key': 'test_object.json',
            },
            'Body': None,
        }
        cls.test_builder = Builder(cls.test_config, cls.test_operation)

    def test_parse_request_params(self):
        test_params = self.test_builder.parse_request_params()
        self.assertEqual(test_params['test_params_1'], 'test_val')
        self.assertEqual(test_params['test_params_2'], 'test_val')

    def test_parse_request_headers(self):
        test_headers = self.test_builder.parse_request_headers()
        self.assertEqual(test_headers['Host'], 'pek3a.qingstor.com')
        self.assertEqual(test_headers['Date'], 'Wed, 10 Dec 2014 17:20:31 GMT')
        self.assertEqual(
            test_headers['User-Agent'],
            ('qingstor-sdk-python/{sdk_version}  '
             '(Python v{python_version}; {system})').format(
                 sdk_version=__version__,
                 python_version=platform.python_version(),
                 system=sys.platform))
        self.assertEqual(test_headers['Content-Type'], 'application/json')

    def test_parse_request_body(self):
        test_body = self.test_builder.parse_request_body()
        self.assertEqual(
            test_body,
            json.dumps(
                {
                    'test_elements_1': 'test_val',
                    'test_elements_2': 'test_val',
                    'test_elements_empty': '',
                },
                sort_keys=True))

    def test_parse_request_properties(self):
        test_properties = self.test_builder.parse_request_properties()
        self.assertEqual(test_properties['zone'], 'pek3a')
        self.assertEqual(test_properties['bucket-name'], 'test_bucket')
        self.assertEqual(test_properties['object-key'], 'test_object.json')

    def test_parss_request_uri(self):
        test_uri = self.test_builder.parse_request_uri()
        self.assertEqual(test_uri,
                         ('https://pek3a.qingstor.com:443'
                          '/test_bucket/test_object.json'
                          '?test_params_1=test_val&test_params_2=test_val'))

    def test_parse(self):
        self.maxDiff = None
        test_parse = self.test_builder.parse()
        self.assertEquals(test_parse.data, ('{'
                                            '"test_elements_1": "test_val", '
                                            '"test_elements_2": "test_val", '
                                            '"test_elements_empty": ""'
                                            '}'))
        self.assertEqual(test_parse.headers['Host'], 'pek3a.qingstor.com')
        self.assertEqual(test_parse.headers['Date'],
                         'Wed, 10 Dec 2014 17:20:31 GMT')
        self.assertEqual(
            test_parse.headers['User-Agent'],
            ('qingstor-sdk-python/{sdk_version}  '
             '(Python v{python_version}; {system})').format(
                 sdk_version=__version__,
                 python_version=platform.python_version(),
                 system=sys.platform))
        self.assertEqual(test_parse.headers['Content-Type'], 'application/json')
        self.assertEquals(test_parse.method, 'GET')
        self.assertEquals(test_parse.url,
                          ('https://pek3a.qingstor.com:443'
                           '/test_bucket/test_object.json'
                           '?test_params_1=test_val&test_params_2=test_val'))
