import unittest

from qingstor.sdk.config import Config


class ConfigTestCase(unittest.TestCase):

    def test_init_without_key(self):
        test_config = Config()
        self.assertEqual(test_config.access_key_id, '')
        self.assertEqual(test_config.secret_access_key, '')
        self.assertEqual(test_config.host, 'qingstor.com')
        self.assertEqual(test_config.port, 443)
        self.assertEqual(test_config.protocol, 'https')
        self.assertEqual(test_config.connection_retries, 3)
        self.assertEqual(test_config.log_level, 'warn')

    def test_init_with_key(self):
        test_config = Config('test_access_key_id', 'test_secret_access_key')
        self.assertEqual(test_config.access_key_id, 'test_access_key_id')
        self.assertEqual(test_config.secret_access_key,
                         'test_secret_access_key')
        self.assertEqual(test_config.host, 'qingstor.com')
        self.assertEqual(test_config.port, 443)
        self.assertEqual(test_config.protocol, 'https')
        self.assertEqual(test_config.connection_retries, 3)
        self.assertEqual(test_config.log_level, 'warn')

    def test_init_with_data(self):
        config_data = {
            'access_key_id': 'ACCESS_KEY_ID_1',
            'secret_access_key': 'SECRET_ACCESS_KEY_1',
            'host': 'private.com',
            'port': 80,
            'protocol': 'http',
            'connection_retries': 1,
            'log_level': 'info'
        }
        test_config = Config().load_config_from_data(config_data)
        self.assertEqual(test_config.access_key_id, 'ACCESS_KEY_ID_1')
        self.assertEqual(test_config.secret_access_key, 'SECRET_ACCESS_KEY_1')
        self.assertEqual(test_config.host, 'private.com')
        self.assertEqual(test_config.port, 80)
        self.assertEqual(test_config.protocol, 'http')
        self.assertEqual(test_config.connection_retries, 1)
        self.assertEqual(test_config.log_level, 'info')
