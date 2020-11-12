# +-------------------------------------------------------------------------
# | Copyright (C) 2016 Yunify, Inc.
# +-------------------------------------------------------------------------
# | Licensed under the Apache License, Version 2.0 (the "License");
# | you may not use this work except in compliance with the License.
# | You may obtain a copy of the License in the LICENSE file, or at:
# |
# | http://www.apache.org/licenses/LICENSE-2.0
# |
# | Unless required by applicable law or agreed to in writing, software
# | distributed under the License is distributed on an "AS IS" BASIS,
# | WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# | See the License for the specific language governing permissions and
# | limitations under the License.
# +-------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from ..unpack import Unpacker
from ..request import Request
from ..error import ParameterRequiredError, ParameterValueNotAllowedError


class Bucket(object):

    def __init__(self, config, properties, client):
        # Zone should be forced to lower case
        if properties and "zone" in properties:
            properties["zone"] = properties["zone"].lower()

        self.config = config
        self.properties = properties
        self.client = client

    def delete_request(self):
        operation = {
            "API": "DeleteBucket",
            "Method": "DELETE",
            "URI": "/<bucket-name>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_validate(operation)
        return Request(self.config, operation)

    def delete(self):
        req = self.delete_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_validate(op):
        pass

    def delete_cname_request(self, domain=""):
        operation = {
            "API": "DeleteBucketCNAME",
            "Method": "DELETE",
            "URI": "/<bucket-name>?cname",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "domain": domain,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_cname_validate(operation)
        return Request(self.config, operation)

    def delete_cname(self, domain=""):
        req = self.delete_cname_request(domain=domain)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_cname_validate(op):
        if op["Elements"]["domain"] and not op["Elements"]["domain"]:
            raise ParameterRequiredError("domain", "DeleteBucketCNAMEInput")
        pass

    def delete_cors_request(self):
        operation = {
            "API": "DeleteBucketCORS",
            "Method": "DELETE",
            "URI": "/<bucket-name>?cors",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_cors_validate(operation)
        return Request(self.config, operation)

    def delete_cors(self):
        req = self.delete_cors_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_cors_validate(op):
        pass

    def delete_external_mirror_request(self):
        operation = {
            "API": "DeleteBucketExternalMirror",
            "Method": "DELETE",
            "URI": "/<bucket-name>?mirror",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_external_mirror_validate(operation)
        return Request(self.config, operation)

    def delete_external_mirror(self):
        req = self.delete_external_mirror_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_external_mirror_validate(op):
        pass

    def delete_lifecycle_request(self):
        operation = {
            "API": "DeleteBucketLifecycle",
            "Method": "DELETE",
            "URI": "/<bucket-name>?lifecycle",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_lifecycle_validate(operation)
        return Request(self.config, operation)

    def delete_lifecycle(self):
        req = self.delete_lifecycle_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_lifecycle_validate(op):
        pass

    def delete_logging_request(self):
        operation = {
            "API": "DeleteBucketLogging",
            "Method": "DELETE",
            "URI": "/<bucket-name>?logging",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_logging_validate(operation)
        return Request(self.config, operation)

    def delete_logging(self):
        req = self.delete_logging_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_logging_validate(op):
        pass

    def delete_notification_request(self):
        operation = {
            "API": "DeleteBucketNotification",
            "Method": "DELETE",
            "URI": "/<bucket-name>?notification",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_notification_validate(operation)
        return Request(self.config, operation)

    def delete_notification(self):
        req = self.delete_notification_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_notification_validate(op):
        pass

    def delete_policy_request(self):
        operation = {
            "API": "DeleteBucketPolicy",
            "Method": "DELETE",
            "URI": "/<bucket-name>?policy",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_policy_validate(operation)
        return Request(self.config, operation)

    def delete_policy(self):
        req = self.delete_policy_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_policy_validate(op):
        pass

    def delete_replication_request(self):
        operation = {
            "API": "DeleteBucketReplication",
            "Method": "DELETE",
            "URI": "/<bucket-name>?replication",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_replication_validate(operation)
        return Request(self.config, operation)

    def delete_replication(self):
        req = self.delete_replication_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_replication_validate(op):
        pass

    def delete_multiple_objects_request(
        self, content_md5="", objects=list(), quiet=None
    ):
        operation = {
            "API": "DeleteMultipleObjects",
            "Method": "POST",
            "URI": "/<bucket-name>?delete",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "Content-MD5": content_md5,
            },
            "Params": {},
            "Elements": {
                "objects": objects,
                "quiet": quiet,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_multiple_objects_validate(operation)
        return Request(self.config, operation)

    def delete_multiple_objects(
        self, content_md5="", objects=list(), quiet=None
    ):
        req = self.delete_multiple_objects_request(
            content_md5=content_md5, objects=objects, quiet=quiet
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_multiple_objects_validate(op):
        if op["Headers"]["Content-MD5"] and not op["Headers"]["Content-MD5"]:
            raise ParameterRequiredError(
                "Content-MD5", "DeleteMultipleObjectsInput"
            )
        if "objects" not in op["Elements"] and not op["Elements"]["objects"]:
            raise ParameterRequiredError(
                "objects", "DeleteMultipleObjectsInput"
            )
        for x in op["Elements"]["objects"]:
            pass
        pass

    def get_acl_request(self):
        operation = {
            "API": "GetBucketACL",
            "Method": "GET",
            "URI": "/<bucket-name>?acl",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_acl_validate(operation)
        return Request(self.config, operation)

    def get_acl(self):
        req = self.get_acl_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_acl_validate(op):
        pass

    def get_cname_request(self, type=""):
        operation = {
            "API": "GetBucketCNAME",
            "Method": "GET",
            "URI": "/<bucket-name>?cname",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {
                "type": type,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_cname_validate(operation)
        return Request(self.config, operation)

    def get_cname(self, type=""):
        req = self.get_cname_request(type=type)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_cname_validate(op):
        if op["Params"]["type"] and not op["Params"]["type"]:
            type_valid_values = ["website", "normal"]
            if str(op["Params"]["type"]) not in type_valid_values:
                raise ParameterValueNotAllowedError(
                    "type", op["Params"]["type"], type_valid_values
                )
        pass

    def get_cors_request(self):
        operation = {
            "API": "GetBucketCORS",
            "Method": "GET",
            "URI": "/<bucket-name>?cors",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_cors_validate(operation)
        return Request(self.config, operation)

    def get_cors(self):
        req = self.get_cors_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_cors_validate(op):
        pass

    def get_external_mirror_request(self):
        operation = {
            "API": "GetBucketExternalMirror",
            "Method": "GET",
            "URI": "/<bucket-name>?mirror",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_external_mirror_validate(operation)
        return Request(self.config, operation)

    def get_external_mirror(self):
        req = self.get_external_mirror_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_external_mirror_validate(op):
        pass

    def get_lifecycle_request(self):
        operation = {
            "API": "GetBucketLifecycle",
            "Method": "GET",
            "URI": "/<bucket-name>?lifecycle",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_lifecycle_validate(operation)
        return Request(self.config, operation)

    def get_lifecycle(self):
        req = self.get_lifecycle_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_lifecycle_validate(op):
        pass

    def get_logging_request(self):
        operation = {
            "API": "GetBucketLogging",
            "Method": "GET",
            "URI": "/<bucket-name>?logging",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_logging_validate(operation)
        return Request(self.config, operation)

    def get_logging(self):
        req = self.get_logging_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_logging_validate(op):
        pass

    def get_notification_request(self):
        operation = {
            "API": "GetBucketNotification",
            "Method": "GET",
            "URI": "/<bucket-name>?notification",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_notification_validate(operation)
        return Request(self.config, operation)

    def get_notification(self):
        req = self.get_notification_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_notification_validate(op):
        pass

    def get_policy_request(self):
        operation = {
            "API": "GetBucketPolicy",
            "Method": "GET",
            "URI": "/<bucket-name>?policy",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_policy_validate(operation)
        return Request(self.config, operation)

    def get_policy(self):
        req = self.get_policy_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_policy_validate(op):
        pass

    def get_replication_request(self):
        operation = {
            "API": "GetBucketReplication",
            "Method": "GET",
            "URI": "/<bucket-name>?replication",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_replication_validate(operation)
        return Request(self.config, operation)

    def get_replication(self):
        req = self.get_replication_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_replication_validate(op):
        pass

    def get_statistics_request(self):
        operation = {
            "API": "GetBucketStatistics",
            "Method": "GET",
            "URI": "/<bucket-name>?stats",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_statistics_validate(operation)
        return Request(self.config, operation)

    def get_statistics(self):
        req = self.get_statistics_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_statistics_validate(op):
        pass

    def head_request(self):
        operation = {
            "API": "HeadBucket",
            "Method": "HEAD",
            "URI": "/<bucket-name>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.head_bucket_validate(operation)
        return Request(self.config, operation)

    def head(self):
        req = self.head_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def head_bucket_validate(op):
        pass

    def list_multipart_uploads_request(
        self,
        delimiter="",
        key_marker="",
        limit=None,
        prefix="",
        upload_id_marker=""
    ):
        operation = {
            "API": "ListMultipartUploads",
            "Method": "GET",
            "URI": "/<bucket-name>?uploads",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {
                "delimiter": delimiter,
                "key_marker": key_marker,
                "limit": limit,
                "prefix": prefix,
                "upload_id_marker": upload_id_marker,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.list_multipart_uploads_validate(operation)
        return Request(self.config, operation)

    def list_multipart_uploads(
        self,
        delimiter="",
        key_marker="",
        limit=None,
        prefix="",
        upload_id_marker=""
    ):
        req = self.list_multipart_uploads_request(
            delimiter=delimiter,
            key_marker=key_marker,
            limit=limit,
            prefix=prefix,
            upload_id_marker=upload_id_marker
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def list_multipart_uploads_validate(op):
        pass

    def list_objects_request(
        self, delimiter="", limit=None, marker="", prefix=""
    ):
        operation = {
            "API": "ListObjects",
            "Method": "GET",
            "URI": "/<bucket-name>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {
                "delimiter": delimiter,
                "limit": limit,
                "marker": marker,
                "prefix": prefix,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.list_objects_validate(operation)
        return Request(self.config, operation)

    def list_objects(self, delimiter="", limit=None, marker="", prefix=""):
        req = self.list_objects_request(
            delimiter=delimiter, limit=limit, marker=marker, prefix=prefix
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def list_objects_validate(op):
        pass

    def put_request(self):
        operation = {
            "API": "PutBucket",
            "Method": "PUT",
            "URI": "/<bucket-name>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_validate(operation)
        return Request(self.config, operation)

    def put(self):
        req = self.put_request()
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_validate(op):
        pass

    def put_acl_request(self, acl=list()):
        operation = {
            "API": "PutBucketACL",
            "Method": "PUT",
            "URI": "/<bucket-name>?acl",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "acl": acl,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_acl_validate(operation)
        return Request(self.config, operation)

    def put_acl(self, acl=list()):
        req = self.put_acl_request(acl=acl)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_acl_validate(op):
        if "acl" not in op["Elements"] and not op["Elements"]["acl"]:
            raise ParameterRequiredError("acl", "PutBucketACLInput")
        for x in op["Elements"]["acl"]:
            if "grantee" not in x:
                if x["grantee"]["type"] and not x["grantee"]["type"]:
                    raise ParameterRequiredError("type", "grantee")
                if x["grantee"]["type"] and not x["grantee"]["type"]:
                    type_valid_values = ["user", "group"]
                    if str(x["grantee"]["type"]) not in type_valid_values:
                        raise ParameterValueNotAllowedError(
                            "type", x["grantee"]["type"], type_valid_values
                        )
                pass
                if "grantee" not in x:
                    raise ParameterRequiredError("grantee", "acl")
            if x["permission"] and not x["permission"]:
                raise ParameterRequiredError("permission", "acl")
            if x["permission"] and not x["permission"]:
                permission_valid_values = ["READ", "WRITE", "FULL_CONTROL"]
                if str(x["permission"]) not in permission_valid_values:
                    raise ParameterValueNotAllowedError(
                        "permission", x["permission"], permission_valid_values
                    )
            pass
        pass

    def put_cname_request(self, domain="", type=""):
        operation = {
            "API": "PutBucketCNAME",
            "Method": "PUT",
            "URI": "/<bucket-name>?cname",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "domain": domain,
                "type": type,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_cname_validate(operation)
        return Request(self.config, operation)

    def put_cname(self, domain="", type=""):
        req = self.put_cname_request(domain=domain, type=type)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_cname_validate(op):
        if op["Elements"]["domain"] and not op["Elements"]["domain"]:
            raise ParameterRequiredError("domain", "PutBucketCNAMEInput")
        if op["Elements"]["type"] and not op["Elements"]["type"]:
            type_valid_values = ["normal", "website"]
            if str(op["Elements"]["type"]) not in type_valid_values:
                raise ParameterValueNotAllowedError(
                    "type", op["Elements"]["type"], type_valid_values
                )
        pass

    def put_cors_request(self, cors_rules=list()):
        operation = {
            "API": "PutBucketCORS",
            "Method": "PUT",
            "URI": "/<bucket-name>?cors",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "cors_rules": cors_rules,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_cors_validate(operation)
        return Request(self.config, operation)

    def put_cors(self, cors_rules=list()):
        req = self.put_cors_request(cors_rules=cors_rules)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_cors_validate(op):
        if "cors_rules" not in op["Elements"
                                  ] and not op["Elements"]["cors_rules"]:
            raise ParameterRequiredError("cors_rules", "PutBucketCORSInput")
        for x in op["Elements"]["cors_rules"]:
            if "allowed_methods" not in x and not x["allowed_methods"]:
                raise ParameterRequiredError("allowed_methods", "cors_rule")
            if x["allowed_origin"] and not x["allowed_origin"]:
                raise ParameterRequiredError("allowed_origin", "cors_rule")
            pass
        pass

    def put_external_mirror_request(self, source_site=""):
        operation = {
            "API": "PutBucketExternalMirror",
            "Method": "PUT",
            "URI": "/<bucket-name>?mirror",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "source_site": source_site,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_external_mirror_validate(operation)
        return Request(self.config, operation)

    def put_external_mirror(self, source_site=""):
        req = self.put_external_mirror_request(source_site=source_site)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_external_mirror_validate(op):
        if op["Elements"]["source_site"] and not op["Elements"]["source_site"]:
            raise ParameterRequiredError(
                "source_site", "PutBucketExternalMirrorInput"
            )
        pass

    def put_lifecycle_request(self, rule=list()):
        operation = {
            "API": "PutBucketLifecycle",
            "Method": "PUT",
            "URI": "/<bucket-name>?lifecycle",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "rule": rule,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_lifecycle_validate(operation)
        return Request(self.config, operation)

    def put_lifecycle(self, rule=list()):
        req = self.put_lifecycle_request(rule=rule)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_lifecycle_validate(op):
        if "rule" not in op["Elements"] and not op["Elements"]["rule"]:
            raise ParameterRequiredError("rule", "PutBucketLifecycleInput")
        for x in op["Elements"]["rule"]:
            if "abort_incomplete_multipart_upload" not in x:
                if x["abort_incomplete_multipart_upload"
                     ]["days_after_initiation"
                       ] and not x["abort_incomplete_multipart_upload"][
                           "days_after_initiation"]:
                    raise ParameterRequiredError(
                        "days_after_initiation",
                        "abort_incomplete_multipart_upload"
                    )
                pass
            if "expiration" not in x:
                pass
            if "filter" not in x:
                if x["filter"]["prefix"] and not x["filter"]["prefix"]:
                    raise ParameterRequiredError("prefix", "filter")
                pass
                if "filter" not in x:
                    raise ParameterRequiredError("filter", "rule")
            if x["id"] and not x["id"]:
                raise ParameterRequiredError("id", "rule")
            if x["status"] and not x["status"]:
                raise ParameterRequiredError("status", "rule")
            if x["status"] and not x["status"]:
                status_valid_values = ["enabled", "disabled"]
                if str(x["status"]) not in status_valid_values:
                    raise ParameterValueNotAllowedError(
                        "status", x["status"], status_valid_values
                    )
            if "transition" not in x:
                if x["transition"]["storage_class"
                                   ] and not x["transition"]["storage_class"]:
                    raise ParameterRequiredError("storage_class", "transition")
                pass
            pass
        pass

    def put_logging_request(self, target_bucket="", target_prefix=""):
        operation = {
            "API": "PutBucketLogging",
            "Method": "PUT",
            "URI": "/<bucket-name>?logging",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "target_bucket": target_bucket,
                "target_prefix": target_prefix,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_logging_validate(operation)
        return Request(self.config, operation)

    def put_logging(self, target_bucket="", target_prefix=""):
        req = self.put_logging_request(
            target_bucket=target_bucket, target_prefix=target_prefix
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_logging_validate(op):
        if op["Elements"]["target_bucket"
                          ] and not op["Elements"]["target_bucket"]:
            raise ParameterRequiredError(
                "target_bucket", "PutBucketLoggingInput"
            )
        if op["Elements"]["target_prefix"
                          ] and not op["Elements"]["target_prefix"]:
            raise ParameterRequiredError(
                "target_prefix", "PutBucketLoggingInput"
            )
        pass

    def put_notification_request(self, notifications=list()):
        operation = {
            "API": "PutBucketNotification",
            "Method": "PUT",
            "URI": "/<bucket-name>?notification",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "notifications": notifications,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_notification_validate(operation)
        return Request(self.config, operation)

    def put_notification(self, notifications=list()):
        req = self.put_notification_request(notifications=notifications)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_notification_validate(op):
        if "notifications" not in op["Elements"
                                     ] and not op["Elements"]["notifications"]:
            raise ParameterRequiredError(
                "notifications", "PutBucketNotificationInput"
            )
        for x in op["Elements"]["notifications"]:
            if x["cloudfunc"] and not x["cloudfunc"]:
                raise ParameterRequiredError("cloudfunc", "notification")
            if x["cloudfunc"] and not x["cloudfunc"]:
                cloudfunc_valid_values = ["tupu-porn", "notifier", "image"]
                if str(x["cloudfunc"]) not in cloudfunc_valid_values:
                    raise ParameterValueNotAllowedError(
                        "cloudfunc", x["cloudfunc"], cloudfunc_valid_values
                    )
            if "cloudfunc_args" not in x:
                if x["cloudfunc_args"]["action"
                                       ] and not x["cloudfunc_args"]["action"]:
                    raise ParameterRequiredError("action", "cloudfunc_args")
                pass
            if "event_types" not in x and not x["event_types"]:
                raise ParameterRequiredError("event_types", "notification")
            if x["id"] and not x["id"]:
                raise ParameterRequiredError("id", "notification")
            pass
        pass

    def put_policy_request(self, statement=list()):
        operation = {
            "API": "PutBucketPolicy",
            "Method": "PUT",
            "URI": "/<bucket-name>?policy",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "statement": statement,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_policy_validate(operation)
        return Request(self.config, operation)

    def put_policy(self, statement=list()):
        req = self.put_policy_request(statement=statement)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_policy_validate(op):
        if "statement" not in op["Elements"] and not op["Elements"]["statement"]:
            raise ParameterRequiredError("statement", "PutBucketPolicyInput")
        for x in op["Elements"]["statement"]:
            if "action" not in x and not x["action"]:
                raise ParameterRequiredError("action", "statement")
            if "condition" not in x:
                if "ip_address" not in x["condition"]:
                    pass
                if "is_null" not in x["condition"]:
                    pass
                if "not_ip_address" not in x["condition"]:
                    pass
                if "string_like" not in x["condition"]:
                    pass
                if "string_not_like" not in x["condition"]:
                    pass
                pass
            if x["effect"] and not x["effect"]:
                raise ParameterRequiredError("effect", "statement")
            if x["effect"] and not x["effect"]:
                effect_valid_values = ["allow", "deny"]
                if str(x["effect"]) not in effect_valid_values:
                    raise ParameterValueNotAllowedError(
                        "effect", x["effect"], effect_valid_values
                    )
            if x["id"] and not x["id"]:
                raise ParameterRequiredError("id", "statement")
            if "user" not in x and not x["user"]:
                raise ParameterRequiredError("user", "statement")
            pass
        pass

    def put_replication_request(self, rules=list()):
        operation = {
            "API": "PutBucketReplication",
            "Method": "PUT",
            "URI": "/<bucket-name>?replication",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {
                "rules": rules,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_replication_validate(operation)
        return Request(self.config, operation)

    def put_replication(self, rules=list()):
        req = self.put_replication_request(rules=rules)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_replication_validate(op):
        if "rules" not in op["Elements"] and not op["Elements"]["rules"]:
            raise ParameterRequiredError("rules", "PutBucketReplicationInput")
        for x in op["Elements"]["rules"]:
            if x["delete_marker"] and not x["delete_marker"]:
                delete_marker_valid_values = ["enabled", "disabled"]
                if str(x["delete_marker"]) not in delete_marker_valid_values:
                    raise ParameterValueNotAllowedError(
                        "delete_marker", x["delete_marker"],
                        delete_marker_valid_values
                    )
            if "destination" not in x:
                if x["destination"]["bucket"] and not x["destination"]["bucket"]:
                    raise ParameterRequiredError("bucket", "destination")
                pass
                if "destination" not in x:
                    raise ParameterRequiredError("destination", "rules")
            if "filters" not in x:
                pass
                if "filters" not in x:
                    raise ParameterRequiredError("filters", "rules")
            if x["id"] and not x["id"]:
                raise ParameterRequiredError("id", "rules")
            if x["status"] and not x["status"]:
                status_valid_values = ["enabled", "disabled"]
                if str(x["status"]) not in status_valid_values:
                    raise ParameterValueNotAllowedError(
                        "status", x["status"], status_valid_values
                    )
            if x["sync_marker"] and not x["sync_marker"]:
                sync_marker_valid_values = ["enabled", "disabled"]
                if str(x["sync_marker"]) not in sync_marker_valid_values:
                    raise ParameterValueNotAllowedError(
                        "sync_marker", x["sync_marker"],
                        sync_marker_valid_values
                    )
            pass
        pass

    def abort_multipart_upload_request(self, object_key, upload_id=""):
        operation = {
            "API": "AbortMultipartUpload",
            "Method": "DELETE",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {
                "upload_id": upload_id,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        self.abort_multipart_upload_validate(operation)
        return Request(self.config, operation)

    def abort_multipart_upload(self, object_key, upload_id=""):
        req = self.abort_multipart_upload_request(
            object_key, upload_id=upload_id
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def abort_multipart_upload_validate(op):
        if op["Params"]["upload_id"] and not op["Params"]["upload_id"]:
            raise ParameterRequiredError(
                "upload_id", "AbortMultipartUploadInput"
            )
        pass

    def append_object_request(
        self,
        object_key,
        position=None,
        content_length=None,
        content_md5="",
        content_type="",
        x_qs_storage_class="",
        body=None
    ):
        operation = {
            "API": "AppendObject",
            "Method": "POST",
            "URI": "/<bucket-name>/<object-key>?append",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "Content-Length": content_length,
                "Content-MD5": content_md5,
                "Content-Type": content_type,
                "X-QS-Storage-Class": x_qs_storage_class,
            },
            "Params": {
                "position": position,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": body
        }
        operation["Properties"]["object-key"] = object_key
        self.append_object_validate(operation)
        return Request(self.config, operation)

    def append_object(
        self,
        object_key,
        position=None,
        content_length=None,
        content_md5="",
        content_type="",
        x_qs_storage_class="",
        body=None
    ):
        req = self.append_object_request(
            object_key,
            position=position,
            content_length=content_length,
            content_md5=content_md5,
            content_type=content_type,
            x_qs_storage_class=x_qs_storage_class,
            body=body
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def append_object_validate(op):
        if op["Params"]["position"] and not op["Params"]["position"]:
            raise ParameterRequiredError("position", "AppendObjectInput")
        if op["Headers"]["X-QS-Storage-Class"
                         ] and not op["Headers"]["X-QS-Storage-Class"]:
            x_qs_storage_class_valid_values = ["STANDARD", "STANDARD_IA"]
            if str(op["Headers"]["X-QS-Storage-Class"]
                   ) not in x_qs_storage_class_valid_values:
                raise ParameterValueNotAllowedError(
                    "X-QS-Storage-Class", op["Headers"]["X-QS-Storage-Class"],
                    x_qs_storage_class_valid_values
                )
        pass

    def complete_multipart_upload_request(
        self,
        object_key,
        upload_id="",
        etag="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5="",
        object_parts=list()
    ):
        operation = {
            "API": "CompleteMultipartUpload",
            "Method": "POST",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "ETag":
                etag,
                "X-QS-Encryption-Customer-Algorithm":
                x_qs_encryption_customer_algorithm,
                "X-QS-Encryption-Customer-Key":
                x_qs_encryption_customer_key,
                "X-QS-Encryption-Customer-Key-MD5":
                x_qs_encryption_customer_key_md5,
            },
            "Params": {
                "upload_id": upload_id,
            },
            "Elements": {
                "object_parts": object_parts,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        self.complete_multipart_upload_validate(operation)
        return Request(self.config, operation)

    def complete_multipart_upload(
        self,
        object_key,
        upload_id="",
        etag="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5="",
        object_parts=list()
    ):
        req = self.complete_multipart_upload_request(
            object_key,
            upload_id=upload_id,
            etag=etag,
            x_qs_encryption_customer_algorithm=
            x_qs_encryption_customer_algorithm,
            x_qs_encryption_customer_key=x_qs_encryption_customer_key,
            x_qs_encryption_customer_key_md5=x_qs_encryption_customer_key_md5,
            object_parts=object_parts
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def complete_multipart_upload_validate(op):
        if op["Params"]["upload_id"] and not op["Params"]["upload_id"]:
            raise ParameterRequiredError(
                "upload_id", "CompleteMultipartUploadInput"
            )
        if "object_parts" not in op["Elements"
                                    ] and not op["Elements"]["object_parts"]:
            raise ParameterRequiredError(
                "object_parts", "CompleteMultipartUploadInput"
            )
        for x in op["Elements"]["object_parts"]:
            if x["part_number"] and not x["part_number"]:
                raise ParameterRequiredError("part_number", "object_part")
            pass
        pass

    def delete_object_request(self, object_key):
        operation = {
            "API": "DeleteObject",
            "Method": "DELETE",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        self.delete_object_validate(operation)
        return Request(self.config, operation)

    def delete_object(self, object_key):
        req = self.delete_object_request(object_key)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_object_validate(op):
        pass

    def get_object_request(
        self,
        object_key,
        response_cache_control="",
        response_content_disposition="",
        response_content_encoding="",
        response_content_language="",
        response_content_type="",
        response_expires="",
        if_match="",
        if_modified_since="",
        if_none_match="",
        if_unmodified_since="",
        range="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5=""
    ):
        operation = {
            "API": "GetObject",
            "Method": "GET",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "If-Match":
                if_match,
                "If-Modified-Since":
                if_modified_since,
                "If-None-Match":
                if_none_match,
                "If-Unmodified-Since":
                if_unmodified_since,
                "Range":
                range,
                "X-QS-Encryption-Customer-Algorithm":
                x_qs_encryption_customer_algorithm,
                "X-QS-Encryption-Customer-Key":
                x_qs_encryption_customer_key,
                "X-QS-Encryption-Customer-Key-MD5":
                x_qs_encryption_customer_key_md5,
            },
            "Params": {
                "response-cache-control": response_cache_control,
                "response-content-disposition": response_content_disposition,
                "response-content-encoding": response_content_encoding,
                "response-content-language": response_content_language,
                "response-content-type": response_content_type,
                "response-expires": response_expires,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        self.get_object_validate(operation)
        return Request(self.config, operation)

    def get_object(
        self,
        object_key,
        response_cache_control="",
        response_content_disposition="",
        response_content_encoding="",
        response_content_language="",
        response_content_type="",
        response_expires="",
        if_match="",
        if_modified_since="",
        if_none_match="",
        if_unmodified_since="",
        range="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5=""
    ):
        req = self.get_object_request(
            object_key,
            response_cache_control=response_cache_control,
            response_content_disposition=response_content_disposition,
            response_content_encoding=response_content_encoding,
            response_content_language=response_content_language,
            response_content_type=response_content_type,
            response_expires=response_expires,
            if_match=if_match,
            if_modified_since=if_modified_since,
            if_none_match=if_none_match,
            if_unmodified_since=if_unmodified_since,
            range=range,
            x_qs_encryption_customer_algorithm=
            x_qs_encryption_customer_algorithm,
            x_qs_encryption_customer_key=x_qs_encryption_customer_key,
            x_qs_encryption_customer_key_md5=x_qs_encryption_customer_key_md5
        )
        resp = self.client.send(req.sign(), stream=True)
        return Unpacker(resp)

    @staticmethod
    def get_object_validate(op):
        pass

    def head_object_request(
        self,
        object_key,
        if_match="",
        if_modified_since="",
        if_none_match="",
        if_unmodified_since="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5=""
    ):
        operation = {
            "API": "HeadObject",
            "Method": "HEAD",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "If-Match":
                if_match,
                "If-Modified-Since":
                if_modified_since,
                "If-None-Match":
                if_none_match,
                "If-Unmodified-Since":
                if_unmodified_since,
                "X-QS-Encryption-Customer-Algorithm":
                x_qs_encryption_customer_algorithm,
                "X-QS-Encryption-Customer-Key":
                x_qs_encryption_customer_key,
                "X-QS-Encryption-Customer-Key-MD5":
                x_qs_encryption_customer_key_md5,
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        self.head_object_validate(operation)
        return Request(self.config, operation)

    def head_object(
        self,
        object_key,
        if_match="",
        if_modified_since="",
        if_none_match="",
        if_unmodified_since="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5=""
    ):
        req = self.head_object_request(
            object_key,
            if_match=if_match,
            if_modified_since=if_modified_since,
            if_none_match=if_none_match,
            if_unmodified_since=if_unmodified_since,
            x_qs_encryption_customer_algorithm=
            x_qs_encryption_customer_algorithm,
            x_qs_encryption_customer_key=x_qs_encryption_customer_key,
            x_qs_encryption_customer_key_md5=x_qs_encryption_customer_key_md5
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def head_object_validate(op):
        pass

    def image_process_request(
        self,
        object_key,
        action="",
        response_cache_control="",
        response_content_disposition="",
        response_content_encoding="",
        response_content_language="",
        response_content_type="",
        response_expires="",
        if_modified_since=""
    ):
        operation = {
            "API": "ImageProcess",
            "Method": "GET",
            "URI": "/<bucket-name>/<object-key>?image",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "If-Modified-Since": if_modified_since,
            },
            "Params": {
                "action": action,
                "response-cache-control": response_cache_control,
                "response-content-disposition": response_content_disposition,
                "response-content-encoding": response_content_encoding,
                "response-content-language": response_content_language,
                "response-content-type": response_content_type,
                "response-expires": response_expires,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        self.image_process_validate(operation)
        return Request(self.config, operation)

    def image_process(
        self,
        object_key,
        action="",
        response_cache_control="",
        response_content_disposition="",
        response_content_encoding="",
        response_content_language="",
        response_content_type="",
        response_expires="",
        if_modified_since=""
    ):
        req = self.image_process_request(
            object_key,
            action=action,
            response_cache_control=response_cache_control,
            response_content_disposition=response_content_disposition,
            response_content_encoding=response_content_encoding,
            response_content_language=response_content_language,
            response_content_type=response_content_type,
            response_expires=response_expires,
            if_modified_since=if_modified_since
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def image_process_validate(op):
        if op["Params"]["action"] and not op["Params"]["action"]:
            raise ParameterRequiredError("action", "ImageProcessInput")
        pass

    def initiate_multipart_upload_request(
        self,
        object_key,
        content_type="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5="",
        x_qs_meta_data=dict(),
        x_qs_storage_class=""
    ):
        operation = {
            "API": "InitiateMultipartUpload",
            "Method": "POST",
            "URI": "/<bucket-name>/<object-key>?uploads",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "Content-Type": content_type,
                "X-QS-Encryption-Customer-Algorithm":
                x_qs_encryption_customer_algorithm,
                "X-QS-Encryption-Customer-Key": x_qs_encryption_customer_key,
                "X-QS-Encryption-Customer-Key-MD5":
                x_qs_encryption_customer_key_md5,
                "X-QS-MetaData": x_qs_meta_data,
                "X-QS-Storage-Class": x_qs_storage_class,
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        self.initiate_multipart_upload_validate(operation)
        return Request(self.config, operation)

    def initiate_multipart_upload(
        self,
        object_key,
        content_type="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5="",
        x_qs_meta_data=dict(),
        x_qs_storage_class=""
    ):
        req = self.initiate_multipart_upload_request(
            object_key,
            content_type=content_type,
            x_qs_encryption_customer_algorithm=
            x_qs_encryption_customer_algorithm,
            x_qs_encryption_customer_key=x_qs_encryption_customer_key,
            x_qs_encryption_customer_key_md5=x_qs_encryption_customer_key_md5,
            x_qs_meta_data=x_qs_meta_data,
            x_qs_storage_class=x_qs_storage_class
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def initiate_multipart_upload_validate(op):
        if op["Headers"]["X-QS-Storage-Class"
                         ] and not op["Headers"]["X-QS-Storage-Class"]:
            x_qs_storage_class_valid_values = ["STANDARD", "STANDARD_IA"]
            if str(op["Headers"]["X-QS-Storage-Class"]
                   ) not in x_qs_storage_class_valid_values:
                raise ParameterValueNotAllowedError(
                    "X-QS-Storage-Class", op["Headers"]["X-QS-Storage-Class"],
                    x_qs_storage_class_valid_values
                )
        pass

    def list_multipart_request(
        self, object_key, limit=None, part_number_marker=None, upload_id=""
    ):
        operation = {
            "API": "ListMultipart",
            "Method": "GET",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
            },
            "Params": {
                "limit": limit,
                "part_number_marker": part_number_marker,
                "upload_id": upload_id,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        self.list_multipart_validate(operation)
        return Request(self.config, operation)

    def list_multipart(
        self, object_key, limit=None, part_number_marker=None, upload_id=""
    ):
        req = self.list_multipart_request(
            object_key,
            limit=limit,
            part_number_marker=part_number_marker,
            upload_id=upload_id
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def list_multipart_validate(op):
        if op["Params"]["upload_id"] and not op["Params"]["upload_id"]:
            raise ParameterRequiredError("upload_id", "ListMultipartInput")
        pass

    def options_object_request(
        self,
        object_key,
        access_control_request_headers="",
        access_control_request_method="",
        origin=""
    ):
        operation = {
            "API": "OptionsObject",
            "Method": "OPTIONS",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "Access-Control-Request-Headers":
                access_control_request_headers,
                "Access-Control-Request-Method": access_control_request_method,
                "Origin": origin,
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        self.options_object_validate(operation)
        return Request(self.config, operation)

    def options_object(
        self,
        object_key,
        access_control_request_headers="",
        access_control_request_method="",
        origin=""
    ):
        req = self.options_object_request(
            object_key,
            access_control_request_headers=access_control_request_headers,
            access_control_request_method=access_control_request_method,
            origin=origin
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def options_object_validate(op):
        if op["Headers"]["Access-Control-Request-Method"] and not op["Headers"][
                "Access-Control-Request-Method"]:
            raise ParameterRequiredError(
                "Access-Control-Request-Method", "OptionsObjectInput"
            )
        if op["Headers"]["Origin"] and not op["Headers"]["Origin"]:
            raise ParameterRequiredError("Origin", "OptionsObjectInput")
        pass

    def put_object_request(
        self,
        object_key,
        cache_control="",
        content_encoding="",
        content_length=None,
        content_md5="",
        content_type="",
        expect="",
        x_qs_copy_source="",
        x_qs_copy_source_encryption_customer_algorithm="",
        x_qs_copy_source_encryption_customer_key="",
        x_qs_copy_source_encryption_customer_key_md5="",
        x_qs_copy_source_if_match="",
        x_qs_copy_source_if_modified_since="",
        x_qs_copy_source_if_none_match="",
        x_qs_copy_source_if_unmodified_since="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5="",
        x_qs_fetch_if_unmodified_since="",
        x_qs_fetch_source="",
        x_qs_meta_data=dict(),
        x_qs_metadata_directive="",
        x_qs_move_source="",
        x_qs_storage_class="",
        body=None
    ):
        operation = {
            "API": "PutObject",
            "Method": "PUT",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "Cache-Control": cache_control,
                "Content-Encoding": content_encoding,
                "Content-Length": content_length,
                "Content-MD5": content_md5,
                "Content-Type": content_type,
                "Expect": expect,
                "X-QS-Copy-Source": x_qs_copy_source,
                "X-QS-Copy-Source-Encryption-Customer-Algorithm":
                x_qs_copy_source_encryption_customer_algorithm,
                "X-QS-Copy-Source-Encryption-Customer-Key":
                x_qs_copy_source_encryption_customer_key,
                "X-QS-Copy-Source-Encryption-Customer-Key-MD5":
                x_qs_copy_source_encryption_customer_key_md5,
                "X-QS-Copy-Source-If-Match": x_qs_copy_source_if_match,
                "X-QS-Copy-Source-If-Modified-Since":
                x_qs_copy_source_if_modified_since,
                "X-QS-Copy-Source-If-None-Match":
                x_qs_copy_source_if_none_match,
                "X-QS-Copy-Source-If-Unmodified-Since":
                x_qs_copy_source_if_unmodified_since,
                "X-QS-Encryption-Customer-Algorithm":
                x_qs_encryption_customer_algorithm,
                "X-QS-Encryption-Customer-Key": x_qs_encryption_customer_key,
                "X-QS-Encryption-Customer-Key-MD5":
                x_qs_encryption_customer_key_md5,
                "X-QS-Fetch-If-Unmodified-Since":
                x_qs_fetch_if_unmodified_since,
                "X-QS-Fetch-Source": x_qs_fetch_source,
                "X-QS-MetaData": x_qs_meta_data,
                "X-QS-Metadata-Directive": x_qs_metadata_directive,
                "X-QS-Move-Source": x_qs_move_source,
                "X-QS-Storage-Class": x_qs_storage_class,
            },
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": body
        }
        operation["Properties"]["object-key"] = object_key
        self.put_object_validate(operation)
        return Request(self.config, operation)

    def put_object(
        self,
        object_key,
        cache_control="",
        content_encoding="",
        content_length=None,
        content_md5="",
        content_type="",
        expect="",
        x_qs_copy_source="",
        x_qs_copy_source_encryption_customer_algorithm="",
        x_qs_copy_source_encryption_customer_key="",
        x_qs_copy_source_encryption_customer_key_md5="",
        x_qs_copy_source_if_match="",
        x_qs_copy_source_if_modified_since="",
        x_qs_copy_source_if_none_match="",
        x_qs_copy_source_if_unmodified_since="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5="",
        x_qs_fetch_if_unmodified_since="",
        x_qs_fetch_source="",
        x_qs_meta_data=dict(),
        x_qs_metadata_directive="",
        x_qs_move_source="",
        x_qs_storage_class="",
        body=None
    ):
        req = self.put_object_request(
            object_key,
            cache_control=cache_control,
            content_encoding=content_encoding,
            content_length=content_length,
            content_md5=content_md5,
            content_type=content_type,
            expect=expect,
            x_qs_copy_source=x_qs_copy_source,
            x_qs_copy_source_encryption_customer_algorithm=
            x_qs_copy_source_encryption_customer_algorithm,
            x_qs_copy_source_encryption_customer_key=
            x_qs_copy_source_encryption_customer_key,
            x_qs_copy_source_encryption_customer_key_md5=
            x_qs_copy_source_encryption_customer_key_md5,
            x_qs_copy_source_if_match=x_qs_copy_source_if_match,
            x_qs_copy_source_if_modified_since=
            x_qs_copy_source_if_modified_since,
            x_qs_copy_source_if_none_match=x_qs_copy_source_if_none_match,
            x_qs_copy_source_if_unmodified_since=
            x_qs_copy_source_if_unmodified_since,
            x_qs_encryption_customer_algorithm=
            x_qs_encryption_customer_algorithm,
            x_qs_encryption_customer_key=x_qs_encryption_customer_key,
            x_qs_encryption_customer_key_md5=x_qs_encryption_customer_key_md5,
            x_qs_fetch_if_unmodified_since=x_qs_fetch_if_unmodified_since,
            x_qs_fetch_source=x_qs_fetch_source,
            x_qs_meta_data=x_qs_meta_data,
            x_qs_metadata_directive=x_qs_metadata_directive,
            x_qs_move_source=x_qs_move_source,
            x_qs_storage_class=x_qs_storage_class,
            body=body
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_object_validate(op):
        if op["Headers"]["X-QS-Metadata-Directive"
                         ] and not op["Headers"]["X-QS-Metadata-Directive"]:
            x_qs_metadata_directive_valid_values = ["COPY", "REPLACE"]
            if str(op["Headers"]["X-QS-Metadata-Directive"]
                   ) not in x_qs_metadata_directive_valid_values:
                raise ParameterValueNotAllowedError(
                    "X-QS-Metadata-Directive",
                    op["Headers"]["X-QS-Metadata-Directive"],
                    x_qs_metadata_directive_valid_values
                )
        if op["Headers"]["X-QS-Storage-Class"
                         ] and not op["Headers"]["X-QS-Storage-Class"]:
            x_qs_storage_class_valid_values = ["STANDARD", "STANDARD_IA"]
            if str(op["Headers"]["X-QS-Storage-Class"]
                   ) not in x_qs_storage_class_valid_values:
                raise ParameterValueNotAllowedError(
                    "X-QS-Storage-Class", op["Headers"]["X-QS-Storage-Class"],
                    x_qs_storage_class_valid_values
                )
        pass

    def upload_multipart_request(
        self,
        object_key,
        part_number=None,
        upload_id="",
        content_length=None,
        content_md5="",
        x_qs_copy_range="",
        x_qs_copy_source="",
        x_qs_copy_source_encryption_customer_algorithm="",
        x_qs_copy_source_encryption_customer_key="",
        x_qs_copy_source_encryption_customer_key_md5="",
        x_qs_copy_source_if_match="",
        x_qs_copy_source_if_modified_since="",
        x_qs_copy_source_if_none_match="",
        x_qs_copy_source_if_unmodified_since="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5="",
        body=None
    ):
        operation = {
            "API": "UploadMultipart",
            "Method": "PUT",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {
                "Host":
                "".join([self.properties["zone"], ".", self.config.host]),
                "Content-Length":
                content_length,
                "Content-MD5":
                content_md5,
                "X-QS-Copy-Range":
                x_qs_copy_range,
                "X-QS-Copy-Source":
                x_qs_copy_source,
                "X-QS-Copy-Source-Encryption-Customer-Algorithm":
                x_qs_copy_source_encryption_customer_algorithm,
                "X-QS-Copy-Source-Encryption-Customer-Key":
                x_qs_copy_source_encryption_customer_key,
                "X-QS-Copy-Source-Encryption-Customer-Key-MD5":
                x_qs_copy_source_encryption_customer_key_md5,
                "X-QS-Copy-Source-If-Match":
                x_qs_copy_source_if_match,
                "X-QS-Copy-Source-If-Modified-Since":
                x_qs_copy_source_if_modified_since,
                "X-QS-Copy-Source-If-None-Match":
                x_qs_copy_source_if_none_match,
                "X-QS-Copy-Source-If-Unmodified-Since":
                x_qs_copy_source_if_unmodified_since,
                "X-QS-Encryption-Customer-Algorithm":
                x_qs_encryption_customer_algorithm,
                "X-QS-Encryption-Customer-Key":
                x_qs_encryption_customer_key,
                "X-QS-Encryption-Customer-Key-MD5":
                x_qs_encryption_customer_key_md5,
            },
            "Params": {
                "part_number": part_number,
                "upload_id": upload_id,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": body
        }
        operation["Properties"]["object-key"] = object_key
        self.upload_multipart_validate(operation)
        return Request(self.config, operation)

    def upload_multipart(
        self,
        object_key,
        part_number=None,
        upload_id="",
        content_length=None,
        content_md5="",
        x_qs_copy_range="",
        x_qs_copy_source="",
        x_qs_copy_source_encryption_customer_algorithm="",
        x_qs_copy_source_encryption_customer_key="",
        x_qs_copy_source_encryption_customer_key_md5="",
        x_qs_copy_source_if_match="",
        x_qs_copy_source_if_modified_since="",
        x_qs_copy_source_if_none_match="",
        x_qs_copy_source_if_unmodified_since="",
        x_qs_encryption_customer_algorithm="",
        x_qs_encryption_customer_key="",
        x_qs_encryption_customer_key_md5="",
        body=None
    ):
        req = self.upload_multipart_request(
            object_key,
            part_number=part_number,
            upload_id=upload_id,
            content_length=content_length,
            content_md5=content_md5,
            x_qs_copy_range=x_qs_copy_range,
            x_qs_copy_source=x_qs_copy_source,
            x_qs_copy_source_encryption_customer_algorithm=
            x_qs_copy_source_encryption_customer_algorithm,
            x_qs_copy_source_encryption_customer_key=
            x_qs_copy_source_encryption_customer_key,
            x_qs_copy_source_encryption_customer_key_md5=
            x_qs_copy_source_encryption_customer_key_md5,
            x_qs_copy_source_if_match=x_qs_copy_source_if_match,
            x_qs_copy_source_if_modified_since=
            x_qs_copy_source_if_modified_since,
            x_qs_copy_source_if_none_match=x_qs_copy_source_if_none_match,
            x_qs_copy_source_if_unmodified_since=
            x_qs_copy_source_if_unmodified_since,
            x_qs_encryption_customer_algorithm=
            x_qs_encryption_customer_algorithm,
            x_qs_encryption_customer_key=x_qs_encryption_customer_key,
            x_qs_encryption_customer_key_md5=x_qs_encryption_customer_key_md5,
            body=body
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def upload_multipart_validate(op):
        if op["Params"]["part_number"] and not op["Params"]["part_number"]:
            raise ParameterRequiredError("part_number", "UploadMultipartInput")
        if op["Params"]["upload_id"] and not op["Params"]["upload_id"]:
            raise ParameterRequiredError("upload_id", "UploadMultipartInput")
        pass
