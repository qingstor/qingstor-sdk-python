import os
import mock
import unittest

from assertpy import assert_that, fail

from qingstor.sdk.service.bucket import Bucket
from qingstor.sdk.client.upload_client import UploadClient
from qingstor.sdk.utils.file_chunk import FileChunk


class MockResponse(dict):

    def __init__(self, **kwargs):
        super(MockResponse, self).__init__()
        self.__dict__ = self
        self["message"] = "Exception"
        for (k, v) in kwargs.items():
            self[k] = v


class MockBucket(Bucket, object):

    def __init__(self, ok):
        super(MockBucket, self).__init__(None, None, None)
        self.ok = ok

    def initiate_multipart_upload(self, *args, **kwargs):
        return MockResponse(ok=self.ok, upload_id="test_upload_id")

    def upload_multipart(self, *args, **kwargs):
        return MockResponse(ok=self.ok, **kwargs)

    def complete_multipart_upload(self, *args, **kwargs):
        return MockResponse(ok=self.ok, **kwargs)

    def abort_multipart_upload(self, *args, **kwargs):
        if self.ok:
            return MockResponse(status_code=400, **kwargs)
        else:
            return MockResponse(status_code=500, **kwargs)

    def list_multipart(self, *args, **kwargs):
        return MockResponse(
            ok=self.ok,
            object_parts=[{
                "part_number": 0
            }, {
                "part_number": 1
            }],
            **kwargs
        )


class TestUploadClient(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ok_upload_client = UploadClient(MockBucket(True))
        cls.error_upload_client = UploadClient(MockBucket(False))
        os.system("dd if=/dev/zero of=test_file bs=1048576 count=1000")

    @classmethod
    def tearDownClass(cls):
        os.system("rm test_file")

    def test_init_upload(self):
        self.ok_upload_client._init_upload("test_file")
        self.assertRaises(
            Exception, self.error_upload_client._init_upload, "test_file"
        )

    def test_upload_part(self):
        self.ok_upload_client._upload_part(
            "test_file", "test_upload_id", 0, "test_data"
        )
        self.assertRaises(
            Exception, self.error_upload_client._upload_part, "test_file",
            "test_upload_id", 0, "test_data"
        )

    def test_continuous_upload_parts(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f)
            self.ok_upload_client._continuous_upload_parts(
                "test_file", fc, "test_upload_id"
            )
            self.assertRaises(
                Exception, self.error_upload_client._continuous_upload_parts,
                "test_file", fc, "test_upload_id"
            )

    def test_differential_upload_parts(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f)
            object_parts = set([0, 1])
            self.ok_upload_client._differential_upload_parts(
                "test_file", fc, "test_upload_id", object_parts
            )
            self.assertRaises(
                Exception, self.error_upload_client._differential_upload_parts,
                "test_file", fc, "test_upload_id", object_parts
            )

    def test_complete_upload(self):
        object_parts = [{"part_number": 0}, {"part_number": 1}]
        self.ok_upload_client._complete_upload(
            "test_file", "test_upload_id", object_parts
        )
        self.assertRaises(
            Exception, self.error_upload_client._complete_upload, "test_file",
            "test_upload_id", object_parts
        )

    def test_abort_upload(self):
        self.ok_upload_client._abort_upload("test_file", "test_upload_id")
        self.assertRaises(
            Exception, self.error_upload_client._abort_upload, "test_file",
            "test_upload_id"
        )

    def test_list_parts(self):
        self.ok_upload_client._list_parts("test_file", "test_upload_id")
        self.assertRaises(
            Exception, self.error_upload_client._list_parts, "test_file",
            "test_upload_id"
        )

    def test_upload(self):
        with open("test_file", "rb") as f:
            self.ok_upload_client.upload("test_file", f)
            self.assertRaises(
                Exception, self.error_upload_client.upload, "test_file", f
            )


if __name__ == "__main__":
    unittest.main()
