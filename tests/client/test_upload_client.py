import os
import mock
import unittest

from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import Bucket
from qingstor.sdk.service.qingstor import QingStor
from qingstor.sdk.client.upload_client import UploadClient
from qingstor.sdk.error import (
    BadRequestError,
    InvalidObjectNameError
)

TEST_PART_SIZE=5242880
TEST_FILE_PATH='test_file_100M'
TEST_OBJECT_KEY='test_upload_20170804'
TEST_ACCESS_KEY='This_is_mock_access_key'
TEST_SECRET_ACCESS_KEY='This_is_mock_secret_access_key'


class MockBucket:

    def __init__(self,status_code):
        self.status_code = status_code

    # Mock the upload_id
    def __getitem__(self, key):
        return 000000000000


class CallbackFunc:

    def __init__(self):
        pass

    def callback_func(self):
        pass

class TestUploadClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        output200=MockBucket(200)
        cls.mock_http200=mock.Mock(return_value=output200)
        output201=MockBucket(201)
        cls.mock_http201=mock.Mock(return_value=output201)
        output400=MockBucket(400)
        cls.mock_http400=mock.Mock(return_value=output400)

        config=Config(TEST_ACCESS_KEY,TEST_SECRET_ACCESS_KEY)
        # QingStor.Bucket=mock_qingstor
        qingstor=QingStor(config)
        # Create bucket instance
        callback_func=CallbackFunc()
        bucket=qingstor.Bucket('test_upload_bucket','pek3a')
        cls.upload_obj = UploadClient(bucket, callback_func.callback_func, TEST_PART_SIZE)


    def setUp(self):
        os.system("dd if=/dev/zero of=test_file_100M bs=1024 count=102400")

    def tearDown(self):
        os.system("rm -f test_file_100M")

    def test_right_response(self):
        # Mock the output of initiate_multipart_upload
        Bucket.initiate_multipart_upload=self.mock_http200
        # Mock the output of upload_multipart
        Bucket.upload_multipart=self.mock_http201
        Bucket.complete_multipart_upload=self.mock_http201
        with open(TEST_FILE_PATH, 'rb') as f:
            self.upload_obj.upload('upload_20180803.mp4', f)

    def test_initialize_bad_response(self):
        # Mock the output of initiate_multipart_upload
        Bucket.initiate_multipart_upload=self.mock_http400

        with open(TEST_FILE_PATH, 'rb') as f:
            self.assertRaises(InvalidObjectNameError,self.upload_obj.upload,TEST_OBJECT_KEY,f)

    def test_upload_bad_response(self):
        # Mock the output of initiate_multipart_upload
        Bucket.initiate_multipart_upload=self.mock_http200

        # Mock the output of upload_multipart
        Bucket.upload_multipart=self.mock_http400

        with open(TEST_FILE_PATH, 'rb') as f:
            self.assertRaises(BadRequestError,self.upload_obj.upload,TEST_OBJECT_KEY,f)


if __name__=="__main__":
    unittest.main()
