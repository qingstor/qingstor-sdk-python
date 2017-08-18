from __future__ import unicode_literals

import os
import unittest

from qingstor.sdk.client.encryption_client import EncryptionClient

RIGHT_OUT_KWARGS = {
    "content_type": "video",
    "x_qs_encryption_customer_algorithm": "AES256",
    "x_qs_encryption_customer_key":
    "MDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDA=",
    "x_qs_encryption_customer_key_md5": "zZ5FnqcIqUjVwvWmyog4zw=="
}


class TestEncryptionFileChunk(unittest.TestCase):

    def test_apply_encryption_headers(self):
        ec = EncryptionClient(
            "test_config", "test_client", "test_bucket", "test_zone", b"0" * 32
        )
        out_kwargs = ec.apply_encrypt_headers(content_type="video")
        self.assertEqual(out_kwargs, RIGHT_OUT_KWARGS)


if __name__ == '__main__':
    unittest.main()
