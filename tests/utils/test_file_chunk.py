from __future__ import print_function

import os
import unittest
from functools import partial

from assertpy import assert_that

from qingstor.sdk.utils.file_chunk import FileChunk
from qingstor.sdk.constant import PART_SIZE, SEGMENT_SIZE

TEST_HOOKS = {"read": [partial(print, "Hello, World")]}


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


if __name__ == "__main__":
    unittest.main()
