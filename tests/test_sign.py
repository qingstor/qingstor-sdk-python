import json
import platform
import sys
import unittest

from qingstor.sdk import __version__
from qingstor.sdk.config import Config
from qingstor.sdk.request import Request


class SignTestCase(unittest.TestCase):

    def setUp(self):
        self.test_config = Config('ACCESS_KEY_ID', 'SECRET_ACCESS_KEY')
        self.test_op = {
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
        self.test_req = Request(self.test_config, self.test_op)

    def test_get_content_md5(self):
        content_md5 = self.test_req.get_content_md5()
        self.assertEqual(content_md5, '')

    def test_get_content_type(self):
        content_type = self.test_req.get_content_type()
        self.assertEqual(content_type, 'application/json')

    def test_get_date(self):
        date = self.test_req.get_date()
        self.assertEqual(date, 'Wed, 10 Dec 2014 17:20:31 GMT')

    def test_get_canonicalized_headers(self):
        canonicalized_headers = self.test_req.get_canonicalized_headers()
        self.assertEqual(canonicalized_headers, '')

    def test_get_canonicalized_resource(self):
        canonicalized_resource = self.test_req.get_canonicalized_resource()
        self.assertEqual(canonicalized_resource,
                         '/test_bucket/test_object.json')

    def test_get_authorization(self):
        authorization = self.test_req.get_authorization()
        self.assertEqual(authorization,
                         'FiEPRBMzn0++U6RagdRMdeLheoipezsZGHoLBw3G9uo=')

    def test_get_query_signature(self):
        authorization = self.test_req.get_query_signature(100)
        self.assertEqual(authorization,
                         'AmmCf9NgkURPxkWiQLuVlonw%2BUK6uhjn%2BsznXdff8A4%3D')

    def test_sign(self):
        req = self.test_req.sign()
        self.assertEquals(req.body, ('{'
                                     '"test_elements_1": "test_val", '
                                     '"test_elements_2": "test_val", '
                                     '"test_elements_empty": ""'
                                     '}'))
        self.assertEqual(req.headers['Content-Length'], '89')
        self.assertEqual(req.headers['Content-Type'], 'application/json')
        self.assertEqual(req.headers['Date'], 'Wed, 10 Dec 2014 17:20:31 GMT')
        self.assertEqual(req.headers['Host'], 'pek3a.qingstor.com')
        self.assertEqual(
            req.headers['User-Agent'],
            ('qingstor-sdk-python/{sdk_version}  '
             '(Python v{python_version}; {system})').format(
                 sdk_version=__version__,
                 python_version=platform.python_version(),
                 system=sys.platform))
        self.assertEqual(req.method, 'GET')
        self.assertEqual(req.url,
                         ('https://pek3a.qingstor.com:443'
                          '/test_bucket/test_object.json'
                          '?test_params_1=test_val&test_params_2=test_val'))

    def test_query_sign(self):
        req = self.test_req.sign_query(100)
        self.assertEquals(req.body, ('{'
                                     '"test_elements_1": "test_val", '
                                     '"test_elements_2": "test_val", '
                                     '"test_elements_empty": ""'
                                     '}'))
        self.assertEqual(req.headers['Content-Length'], '89')
        self.assertEqual(req.headers['Content-Type'], 'application/json')
        self.assertEqual(req.headers['Date'], 'Wed, 10 Dec 2014 17:20:31 GMT')
        self.assertEqual(req.headers['Host'], 'pek3a.qingstor.com')
        self.assertEqual(
            req.headers['User-Agent'],
            ('qingstor-sdk-python/{sdk_version}  '
             '(Python v{python_version}; {system})').format(
                 sdk_version=__version__,
                 python_version=platform.python_version(),
                 system=sys.platform))
        self.assertEqual(req.method, 'GET')
        self.assertEqual(req.url, (
            'https://pek3a.qingstor.com:443/test_bucket/test_object.json?'
            'test_params_1=test_val&test_params_2=test_val'
            '&signature=AmmCf9NgkURPxkWiQLuVlonw%2BUK6uhjn%2BsznXdff8A4%3D'
            '&access_key_id=ACCESS_KEY_ID&expires=100'))
