from ..utils.file_chunk import FileChunk
from ..constant import (PART_SIZE, BINARY_MIME_TYPE)


class UploadClient:
    """UploadClient

    Parameter:
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size(int): the part size users want to partition of the file in byte

    Attributes:
        fd: the source uploading file object
        object_key: the key(usually using file name) of the uploading file
        bucket: bucket refers to bucket object users creating in the QingCloud
        part_size(int): the part size users want to partition of the file in byte

    """

    def __init__(self, bucket, part_size=PART_SIZE):
        self.bucket = bucket
        self.part_size = part_size

    def _init_upload(self, object_key, content_type=BINARY_MIME_TYPE):
        resp = self.bucket.initiate_multipart_upload(
            object_key, content_type=content_type
        )
        if not resp.ok:
            raise Exception(resp["message"])
        return resp["upload_id"]

    def _upload_part(self, object_key, upload_id, index, data):
        resp = self.bucket.upload_multipart(
            object_key, upload_id=upload_id, part_number=index, body=data
        )
        if not resp.ok:
            raise Exception(resp["message"])

    def _continuous_upload_parts(self, object_key, fc, upload_id):
        for (index, data) in enumerate(fc):
            self._upload_part(object_key, upload_id, index, data)
        return [{"part_number": index} for index in range(fc.parts)]

    def _differential_upload_parts(self, object_key, fc, upload_id, parts):
        for index in parts:
            fc.seek(index)
            self._upload_part(object_key, upload_id, index, fc.read_part())
        return [{"part_number": index} for index in range(fc.parts)]

    def _complete_upload(self, object_key, upload_id, parts):
        resp = self.bucket.complete_multipart_upload(
            object_key, upload_id, object_parts=parts
        )
        if not resp.ok:
            raise Exception(resp["message"])

    def _abort_upload(self, object_key, upload_id):
        resp = self.bucket.abort_multipart_upload(
            object_key, upload_id=upload_id
        )
        if not resp.ok:
            raise Exception(resp["message"])

    def _list_parts(self, object_key, upload_id):
        resp = self.bucket.list_multipart(object_key, upload_id=upload_id)
        if not resp.ok:
            raise Exception(resp["message"])
        return resp["object_parts"]

    @staticmethod
    def _cal_difference_parts(local_parts, remote_parts):
        remote_part_numbers = set([
            part["part_number"] for part in remote_parts
        ])
        local_part_numbers = set([part["part_number"] for part in local_parts])
        return local_part_numbers - remote_part_numbers

    def upload(self, object_key, fd, content_type=BINARY_MIME_TYPE, hooks=None):
        fc = FileChunk(fd, self.part_size, hooks)
        upload_id = self._init_upload(object_key, content_type)
        try:
            parts = self._continuous_upload_parts(object_key, fc, upload_id)
            self._complete_upload(object_key, upload_id, parts)
        except:
            self._abort_upload(object_key, upload_id)

    def resume(self, object_key, fd, upload_id, hooks=None):
        fc = FileChunk(fd, self.part_size, hooks)
        diff_parts = self._cal_difference_parts(
            range(fc.parts), self._list_parts(object_key, upload_id)
        )
        try:
            parts = self._differential_upload_parts(
                object_key, fc, upload_id, diff_parts
            )
            self._complete_upload(object_key, upload_id, parts)
        except:
            self._abort_upload(object_key, upload_id)
