import os
import logging

from .file_chunk import FileChunk
from ..constant import (
    HTTP_OK,
    MAX_PARTS,
    HTTP_CREATED,
    HTTP_BAD_REQUEST,
    DEFAULT_PART_SIZE,
    SMALLEST_PART_SIZE
)
from ..error import (
    BadRequestError,
    PartTooSmallError,
    MaxPartsExceededError,
    InvalidObjectNameError
)


class UploadClient:
    """file processing,including open file,move file pointer and read file

    Parameter:
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size(int): the part size users want to partition of the file in byte

    Attributes:
        fd(object): the source uploading file object
        object_key: the key(usually using file name) of the uploading file
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size(int): the part size users want to partition of the file in byte

    """

    def __init__(self, bucket, callback, part_size=DEFAULT_PART_SIZE):
        if (part_size < SMALLEST_PART_SIZE):
            raise PartTooSmallError()
        else:
            self.bucket = bucket
            self.part_size = part_size
            self.logger = logging.getLogger("qingstor-sdk")
            self.callback=callback

    def upload(self, object_key, fd, content_type=""):
        # Initiate multipart upload, create an upload id.
        if content_type == "":
            output = self.bucket.initiate_multipart_upload(object_key)
        else:
            output = self.bucket.initiate_multipart_upload(object_key,content_type)
        if output.status_code == HTTP_BAD_REQUEST:
            raise InvalidObjectNameError()
        elif output.status_code != HTTP_OK:
            self.logger.error("Bad Request!")
            return
        this_upload_id = output['upload_id']
        part_index=0
        part_uploaded_list = []
        file_chunk=FileChunk(fd,self.part_size,self.callback)
        for cur_read_part in file_chunk:
            output = self.bucket.upload_multipart(
                object_key,
                upload_id=this_upload_id,
                part_number=part_index,
                body=cur_read_part)
            if output.status_code == HTTP_CREATED:
                part_uploaded_list += [{"part_number": part_index}]
                part_index += 1
            else:
                raise BadRequestError()
        output=self.bucket.complete_multipart_upload(
            object_key, this_upload_id, object_parts=part_uploaded_list)
        if output.status_code==HTTP_CREATED:
            self.logger.info("Multipart Upload Completed!")
        else:
            raise BadRequestError
