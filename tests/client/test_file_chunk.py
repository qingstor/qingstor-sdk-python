import os
import unittest
from qingstor.sdk.client.file_chunk import FileChunk


# The part size of each reading
TEST_PART_SIZE = 50
TEST_PART_INDEX = 10
# Expected_amount = size(test_small_file.txt)/test_part_size=1024*500/50=10240
EXPECTED_AMOUNT = 10240
TEST_FILE_PATH="test_small_file"

class CallbackFunc:

    def __init__(self):
        pass

    def callback_func(self):
        pass

class TestFileChunk(unittest.TestCase):
    def setUp(self):
        os.system("dd if=/dev/zero of=test_small_file bs=1024 count=500")

    def tearDown(self):
        os.system("rm -f test_small_file")

    def test_next(self):
        callback_func=CallbackFunc()
        with open(TEST_FILE_PATH, 'rb') as f:
            test_file_chunk=FileChunk(f,TEST_PART_SIZE,callback_func.callback_func)
            for cur_read_part in test_file_chunk:
                continue


if __name__=="__main__":
    unittest.main()
