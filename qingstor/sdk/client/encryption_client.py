from __future__ import unicode_literals

import base64

from ..service.bucket import Bucket
from ..utils.helper import md5_digest


class EncryptionClient(Bucket):

    def __init__(
            self,
            config,
            client,
            bucket_name,
            zone,
            encrypt_key,
            encrypt_algo="AES256"
    ):
        properties = {"bucket-name": bucket_name, "zone": zone}
        Bucket.__init__(self, config, properties, client)
        self.encrypt_algo = encrypt_algo
        self.encoded_encrypt_key = base64.b64encode(encrypt_key)
        self.encoded_encrypt_key_md5 = base64.b64encode(md5_digest(encrypt_key))

    def put_object(self, *args, **kwargs):
        kwargs = self.apply_encrypt_headers(**kwargs)
        return Bucket.put_object(self, *args, **kwargs)

    def get_object(self, *args, **kwargs):
        kwargs = self.apply_encrypt_headers(**kwargs)
        return Bucket.get_object(self, *args, **kwargs)

    def head_object(self, *args, **kwargs):
        kwargs = self.apply_encrypt_headers(**kwargs)
        return Bucket.head_object(self, *args, **kwargs)

    def initiate_multipart_upload(self, *args, **kwargs):
        kwargs = self.apply_encrypt_headers(**kwargs)
        return Bucket.initiate_multipart_upload(self, *args, **kwargs)

    def upload_multipart(self, *args, **kwargs):
        kwargs = self.apply_encrypt_headers(**kwargs)
        return Bucket.upload_multipart(self, *args, **kwargs)

    def apply_encrypt_headers(self, **kwargs):
        kwargs["x_qs_encryption_customer_algorithm"] = self.encrypt_algo
        kwargs["x_qs_encryption_customer_key"
               ] = self.encoded_encrypt_key.decode()
        kwargs["x_qs_encryption_customer_key_md5"
               ] = self.encoded_encrypt_key_md5.decode()
        return kwargs
