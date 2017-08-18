from __future__ import print_function

import os
import unittest
from functools import partial

from assertpy import assert_that

from qingstor.sdk.utils.helper import md5_digest
from qingstor.sdk.utils.file_chunk import FileChunk, EncryptionFileChunk
from qingstor.sdk.constant import PART_SIZE, SEGMENT_SIZE

TEST_HOOKS = {"read": [partial(print, "Hello, World")]}
TEST_FILE_NAME = "test_file"
ENCRYPT_KEY = b"0" * 32
ENCRYPT_ALGO = "AES256"
ENCRYPT_KEY_MD5 = b"\xcd\x9eE\x9e\xa7\x08\xa9H\xd5\xc2\xf5\xa6\xca\x888\xcf"
IV = b"0" * 16


class TestFileChunk(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        os.system("dd if=/dev/zero of=test_file bs=1048576 count=1000")

    @classmethod
    def tearDownClass(cls):
        os.system("rm test_file")

    def test_init(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f)

            assert_that(fc.part_size).is_equal_to(64 * 1024 * 1024)
            assert_that(fc.seekable).is_equal_to(True)
            assert_that(fc.hooks).is_equal_to({})
            assert_that(fc.segments).is_equal_to(65536)

    def test_register_hook(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f, hooks=TEST_HOOKS)

            assert_that(fc.hooks).contains_key("read")
            assert_that(fc.hooks["read"]).is_instance_of(list)
            assert_that(callable(fc.hooks["read"][0])).is_true()

    def test_size(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f)

            assert_that(fc.size).is_equal_to(1048576000)

    def test_parts(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f)

            assert_that(fc.parts).is_equal_to(16)

    def test_seek(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f)
            fc.seek(1, os.SEEK_SET)
            assert_that(fc.fd.tell()).is_equal_to(PART_SIZE)

            fc.seek(0, os.SEEK_END)
            data = fc.read()
            assert_that(len(data)).is_equal_to(0)

    def test_read(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f)
            data = fc.read()

            assert_that(len(data)).is_equal_to(SEGMENT_SIZE)

    def test_read_part(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f)
            data = fc.read_part()

            assert_that(len(data)).is_equal_to(PART_SIZE)

    def test_next(self):
        with open("test_file", "rb") as f:
            fc = FileChunk(f)
            index = 0

            for _ in fc:
                index += 1

            assert_that(index).is_equal_to(16)


class TestEncryptionFileChunk(unittest.TestCase):

    def setUp(self):
        os.system("dd if=/dev/zero of=test_file bs=1024 count=500")

    def tearDown(self):
        os.system("rm -f test_file")

    def test_init(self):
        self.assertEqual(md5_digest(ENCRYPT_KEY), ENCRYPT_KEY_MD5)

    def test_read(self):
        with open(TEST_FILE_NAME, "rb") as f:
            efc = EncryptionFileChunk(
                f,
                ENCRYPT_KEY,
                IV,
            )
            read_len = efc.read()
        self.assertEqual(len(read_len), 1024)


if __name__ == "__main__":
    unittest.main()
