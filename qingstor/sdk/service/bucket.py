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
            "Headers": {},
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

    def delete_cname_request(self, domain=None):
        operation = {
            "API": "DeleteBucketCNAME",
            "Method": "DELETE",
            "URI": "/<bucket-name>?cname",
            "Headers": {},
            "Params": {},
            "Elements": {
                "domain": domain,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.delete_bucket_cname_validate(operation)
        return Request(self.config, operation)

    def delete_cname(self, domain=None):
        req = self.delete_cname_request(domain=domain)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_bucket_cname_validate(op):
        if "domain" not in op["Elements"]:
            raise ParameterRequiredError("domain", "DeleteBucketCNAMEInput")
        pass

    def delete_cors_request(self):
        operation = {
            "API": "DeleteBucketCORS",
            "Method": "DELETE",
            "URI": "/<bucket-name>?cors",
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
        self, content_md5=None, objects=None, quiet=None
    ):
        operation = {
            "API": "DeleteMultipleObjects",
            "Method": "POST",
            "URI": "/<bucket-name>?delete",
            "Headers": {},
            "Params": {},
            "Elements": {
                "objects": objects,
                "quiet": quiet,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        if content_md5 is not None:
            operation["Headers"]["Content-MD5"] = content_md5
        self.delete_multiple_objects_validate(operation)
        return Request(self.config, operation)

    def delete_multiple_objects(
        self, content_md5=None, objects=None, quiet=None
    ):
        req = self.delete_multiple_objects_request(
            content_md5=content_md5, objects=objects, quiet=quiet
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def delete_multiple_objects_validate(op):
        if "Content-MD5" not in op["Headers"]:
            raise ParameterRequiredError(
                "Content-MD5", "DeleteMultipleObjectsInput"
            )
        if "objects" not in op["Elements"]:
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
            "Headers": {},
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

    def get_cname_request(self, type=None):
        operation = {
            "API": "GetBucketCNAME",
            "Method": "GET",
            "URI": "/<bucket-name>?cname",
            "Headers": {},
            "Params": {
                "type": type,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.get_bucket_cname_validate(operation)
        return Request(self.config, operation)

    def get_cname(self, type=None):
        req = self.get_cname_request(type=type)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def get_bucket_cname_validate(op):
        if "type" in op["Params"]:
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
            "Headers": {},
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
        delimiter=None,
        key_marker=None,
        limit=None,
        prefix=None,
        upload_id_marker=None
    ):
        operation = {
            "API": "ListMultipartUploads",
            "Method": "GET",
            "URI": "/<bucket-name>?uploads",
            "Headers": {},
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
        delimiter=None,
        key_marker=None,
        limit=None,
        prefix=None,
        upload_id_marker=None
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
        self, delimiter=None, limit=None, marker=None, prefix=None
    ):
        operation = {
            "API": "ListObjects",
            "Method": "GET",
            "URI": "/<bucket-name>",
            "Headers": {},
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

    def list_objects(
        self, delimiter=None, limit=None, marker=None, prefix=None
    ):
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
            "Headers": {},
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

    def put_acl_request(self, acl=None):
        operation = {
            "API": "PutBucketACL",
            "Method": "PUT",
            "URI": "/<bucket-name>?acl",
            "Headers": {},
            "Params": {},
            "Elements": {
                "acl": acl,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_acl_validate(operation)
        return Request(self.config, operation)

    def put_acl(self, acl=None):
        req = self.put_acl_request(acl=acl)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_acl_validate(op):
        if "acl" not in op["Elements"]:
            raise ParameterRequiredError("acl", "PutBucketACLInput")
        for x in op["Elements"]["acl"]:
            if "grantee" not in x:
                raise ParameterRequiredError("grantee", "acl")
            if "grantee" in x:
                if "type" not in x["grantee"]:
                    raise ParameterRequiredError("type", "grantee")
                if "type" in x["grantee"]:
                    type_valid_values = ["user", "group"]
                    if str(x["grantee"]["type"]) not in type_valid_values:
                        raise ParameterValueNotAllowedError(
                            "type", x["grantee"]["type"], type_valid_values
                        )
                pass
            if "permission" not in x:
                raise ParameterRequiredError("permission", "acl")
            if "permission" in x:
                permission_valid_values = ["READ", "WRITE", "FULL_CONTROL"]
                if str(x["permission"]) not in permission_valid_values:
                    raise ParameterValueNotAllowedError(
                        "permission", x["permission"], permission_valid_values
                    )
            pass
        pass

    def put_cname_request(self, domain=None, type=None):
        operation = {
            "API": "PutBucketCNAME",
            "Method": "PUT",
            "URI": "/<bucket-name>?cname",
            "Headers": {},
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

    def put_cname(self, domain=None, type=None):
        req = self.put_cname_request(domain=domain, type=type)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_cname_validate(op):
        if "domain" not in op["Elements"]:
            raise ParameterRequiredError("domain", "PutBucketCNAMEInput")
        if "type" in op["Elements"]:
            type_valid_values = ["normal", "website"]
            if str(op["Elements"]["type"]) not in type_valid_values:
                raise ParameterValueNotAllowedError(
                    "type", op["Elements"]["type"], type_valid_values
                )
        pass

    def put_cors_request(self, cors_rules=None):
        operation = {
            "API": "PutBucketCORS",
            "Method": "PUT",
            "URI": "/<bucket-name>?cors",
            "Headers": {},
            "Params": {},
            "Elements": {
                "cors_rules": cors_rules,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_cors_validate(operation)
        return Request(self.config, operation)

    def put_cors(self, cors_rules=None):
        req = self.put_cors_request(cors_rules=cors_rules)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_cors_validate(op):
        if "cors_rules" not in op["Elements"]:
            raise ParameterRequiredError("cors_rules", "PutBucketCORSInput")
        for x in op["Elements"]["cors_rules"]:
            if "allowed_methods" not in x:
                raise ParameterRequiredError("allowed_methods", "cors_rule")
            if "allowed_origin" not in x:
                raise ParameterRequiredError("allowed_origin", "cors_rule")
            pass
        pass

    def put_external_mirror_request(self, source_site=None):
        operation = {
            "API": "PutBucketExternalMirror",
            "Method": "PUT",
            "URI": "/<bucket-name>?mirror",
            "Headers": {},
            "Params": {},
            "Elements": {
                "source_site": source_site,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_external_mirror_validate(operation)
        return Request(self.config, operation)

    def put_external_mirror(self, source_site=None):
        req = self.put_external_mirror_request(source_site=source_site)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_external_mirror_validate(op):
        if "source_site" not in op["Elements"]:
            raise ParameterRequiredError(
                "source_site", "PutBucketExternalMirrorInput"
            )
        pass

    def put_lifecycle_request(self, rule=None):
        operation = {
            "API": "PutBucketLifecycle",
            "Method": "PUT",
            "URI": "/<bucket-name>?lifecycle",
            "Headers": {},
            "Params": {},
            "Elements": {
                "rule": rule,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_lifecycle_validate(operation)
        return Request(self.config, operation)

    def put_lifecycle(self, rule=None):
        req = self.put_lifecycle_request(rule=rule)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_lifecycle_validate(op):
        if "rule" not in op["Elements"]:
            raise ParameterRequiredError("rule", "PutBucketLifecycleInput")
        for x in op["Elements"]["rule"]:
            if "abort_incomplete_multipart_upload" in x:
                if "days_after_initiation" not in x[
                        "abort_incomplete_multipart_upload"]:
                    raise ParameterRequiredError(
                        "days_after_initiation",
                        "abort_incomplete_multipart_upload"
                    )
                pass
            if "expiration" in x:
                pass
            if "filter" not in x:
                raise ParameterRequiredError("filter", "rule")
            if "filter" in x:
                if "prefix" not in x["filter"]:
                    raise ParameterRequiredError("prefix", "filter")
                pass
            if "id" not in x:
                raise ParameterRequiredError("id", "rule")
            if "status" not in x:
                raise ParameterRequiredError("status", "rule")
            if "status" in x:
                status_valid_values = ["enabled", "disabled"]
                if str(x["status"]) not in status_valid_values:
                    raise ParameterValueNotAllowedError(
                        "status", x["status"], status_valid_values
                    )
            if "transition" in x:
                if "storage_class" not in x["transition"]:
                    raise ParameterRequiredError("storage_class", "transition")
                pass
            pass
        pass

    def put_logging_request(self, target_bucket=None, target_prefix=None):
        operation = {
            "API": "PutBucketLogging",
            "Method": "PUT",
            "URI": "/<bucket-name>?logging",
            "Headers": {},
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

    def put_logging(self, target_bucket=None, target_prefix=None):
        req = self.put_logging_request(
            target_bucket=target_bucket, target_prefix=target_prefix
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_logging_validate(op):
        if "target_bucket" not in op["Elements"]:
            raise ParameterRequiredError(
                "target_bucket", "PutBucketLoggingInput"
            )
        if "target_prefix" not in op["Elements"]:
            raise ParameterRequiredError(
                "target_prefix", "PutBucketLoggingInput"
            )
        pass

    def put_notification_request(self, notifications=None):
        operation = {
            "API": "PutBucketNotification",
            "Method": "PUT",
            "URI": "/<bucket-name>?notification",
            "Headers": {},
            "Params": {},
            "Elements": {
                "notifications": notifications,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_notification_validate(operation)
        return Request(self.config, operation)

    def put_notification(self, notifications=None):
        req = self.put_notification_request(notifications=notifications)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_notification_validate(op):
        if "notifications" not in op["Elements"]:
            raise ParameterRequiredError(
                "notifications", "PutBucketNotificationInput"
            )
        for x in op["Elements"]["notifications"]:
            if "cloudfunc" not in x:
                raise ParameterRequiredError("cloudfunc", "notification")
            if "cloudfunc" in x:
                cloudfunc_valid_values = ["tupu-porn", "notifier", "image"]
                if str(x["cloudfunc"]) not in cloudfunc_valid_values:
                    raise ParameterValueNotAllowedError(
                        "cloudfunc", x["cloudfunc"], cloudfunc_valid_values
                    )
            if "cloudfunc_args" in x:
                if "action" not in x["cloudfunc_args"]:
                    raise ParameterRequiredError("action", "cloudfunc_args")
                pass
            if "event_types" not in x:
                raise ParameterRequiredError("event_types", "notification")
            if "id" not in x:
                raise ParameterRequiredError("id", "notification")
            pass
        pass

    def put_policy_request(self, statement=None):
        operation = {
            "API": "PutBucketPolicy",
            "Method": "PUT",
            "URI": "/<bucket-name>?policy",
            "Headers": {},
            "Params": {},
            "Elements": {
                "statement": statement,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_policy_validate(operation)
        return Request(self.config, operation)

    def put_policy(self, statement=None):
        req = self.put_policy_request(statement=statement)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_policy_validate(op):
        if "statement" not in op["Elements"]:
            raise ParameterRequiredError("statement", "PutBucketPolicyInput")
        for x in op["Elements"]["statement"]:
            if "action" not in x:
                raise ParameterRequiredError("action", "statement")
            if "condition" in x:
                if "ip_address" in x["condition"]:
                    pass
                if "is_null" in x["condition"]:
                    pass
                if "not_ip_address" in x["condition"]:
                    pass
                if "string_like" in x["condition"]:
                    pass
                if "string_not_like" in x["condition"]:
                    pass
                pass
            if "effect" not in x:
                raise ParameterRequiredError("effect", "statement")
            if "effect" in x:
                effect_valid_values = ["allow", "deny"]
                if str(x["effect"]) not in effect_valid_values:
                    raise ParameterValueNotAllowedError(
                        "effect", x["effect"], effect_valid_values
                    )
            if "id" not in x:
                raise ParameterRequiredError("id", "statement")
            if "user" not in x:
                raise ParameterRequiredError("user", "statement")
            pass
        pass

    def put_replication_request(self, rules=None):
        operation = {
            "API": "PutBucketReplication",
            "Method": "PUT",
            "URI": "/<bucket-name>?replication",
            "Headers": {},
            "Params": {},
            "Elements": {
                "rules": rules,
            },
            "Properties": self.properties.copy(),
            "Body": None
        }
        self.put_bucket_replication_validate(operation)
        return Request(self.config, operation)

    def put_replication(self, rules=None):
        req = self.put_replication_request(rules=rules)
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def put_bucket_replication_validate(op):
        if "rules" not in op["Elements"]:
            raise ParameterRequiredError("rules", "PutBucketReplicationInput")
        for x in op["Elements"]["rules"]:
            if "delete_marker" in x:
                delete_marker_valid_values = ["enabled", "disabled"]
                if str(x["delete_marker"]) not in delete_marker_valid_values:
                    raise ParameterValueNotAllowedError(
                        "delete_marker", x["delete_marker"],
                        delete_marker_valid_values
                    )
            if "destination" not in x:
                raise ParameterRequiredError("destination", "rules")
            if "destination" in x:
                if "bucket" not in x["destination"]:
                    raise ParameterRequiredError("bucket", "destination")
                pass
            if "filters" not in x:
                raise ParameterRequiredError("filters", "rules")
            if "filters" in x:
                pass
            if "id" not in x:
                raise ParameterRequiredError("id", "rules")
            if "status" in x:
                status_valid_values = ["enabled", "disabled"]
                if str(x["status"]) not in status_valid_values:
                    raise ParameterValueNotAllowedError(
                        "status", x["status"], status_valid_values
                    )
            if "sync_marker" in x:
                sync_marker_valid_values = ["enabled", "disabled"]
                if str(x["sync_marker"]) not in sync_marker_valid_values:
                    raise ParameterValueNotAllowedError(
                        "sync_marker", x["sync_marker"],
                        sync_marker_valid_values
                    )
            pass
        pass

    def abort_multipart_upload_request(self, object_key, upload_id=None):
        operation = {
            "API": "AbortMultipartUpload",
            "Method": "DELETE",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {},
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

    def abort_multipart_upload(self, object_key, upload_id=None):
        req = self.abort_multipart_upload_request(
            object_key, upload_id=upload_id
        )
        resp = self.client.send(req.sign())
        return Unpacker(resp)

    @staticmethod
    def abort_multipart_upload_validate(op):
        if "upload_id" not in op["Params"]:
            raise ParameterRequiredError(
                "upload_id", "AbortMultipartUploadInput"
            )
        pass

    def append_object_request(
        self,
        object_key,
        position=None,
        content_length=None,
        content_md5=None,
        content_type=None,
        x_qs_storage_class=None,
        body=None
    ):
        operation = {
            "API": "AppendObject",
            "Method": "POST",
            "URI": "/<bucket-name>/<object-key>?append",
            "Headers": {},
            "Params": {
                "position": position,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": body
        }
        operation["Properties"]["object-key"] = object_key
        if content_length is not None:
            operation["Headers"]["Content-Length"] = content_length
        if content_md5 is not None:
            operation["Headers"]["Content-MD5"] = content_md5
        if content_type is not None:
            operation["Headers"]["Content-Type"] = content_type
        if x_qs_storage_class is not None:
            operation["Headers"]["X-QS-Storage-Class"] = x_qs_storage_class
        self.append_object_validate(operation)
        return Request(self.config, operation)

    def append_object(
        self,
        object_key,
        position=None,
        content_length=None,
        content_md5=None,
        content_type=None,
        x_qs_storage_class=None,
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
        if "position" not in op["Params"]:
            raise ParameterRequiredError("position", "AppendObjectInput")
        if "X-QS-Storage-Class" in op["Headers"]:
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
        upload_id=None,
        etag=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None,
        object_parts=None
    ):
        operation = {
            "API": "CompleteMultipartUpload",
            "Method": "POST",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {},
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
        if etag is not None:
            operation["Headers"]["ETag"] = etag
        if x_qs_encryption_customer_algorithm is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Algorithm"
                                 ] = x_qs_encryption_customer_algorithm
        if x_qs_encryption_customer_key is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key"
                                 ] = x_qs_encryption_customer_key
        if x_qs_encryption_customer_key_md5 is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key-MD5"
                                 ] = x_qs_encryption_customer_key_md5
        self.complete_multipart_upload_validate(operation)
        return Request(self.config, operation)

    def complete_multipart_upload(
        self,
        object_key,
        upload_id=None,
        etag=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None,
        object_parts=None
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
        if "upload_id" not in op["Params"]:
            raise ParameterRequiredError(
                "upload_id", "CompleteMultipartUploadInput"
            )
        if "object_parts" not in op["Elements"]:
            raise ParameterRequiredError(
                "object_parts", "CompleteMultipartUploadInput"
            )
        for x in op["Elements"]["object_parts"]:
            if "part_number" not in x:
                raise ParameterRequiredError("part_number", "object_part")
            pass
        pass

    def delete_object_request(self, object_key):
        operation = {
            "API": "DeleteObject",
            "Method": "DELETE",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {},
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
        response_cache_control=None,
        response_content_disposition=None,
        response_content_encoding=None,
        response_content_language=None,
        response_content_type=None,
        response_expires=None,
        if_match=None,
        if_modified_since=None,
        if_none_match=None,
        if_unmodified_since=None,
        range=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None
    ):
        operation = {
            "API": "GetObject",
            "Method": "GET",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {},
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
        if if_match is not None:
            operation["Headers"]["If-Match"] = if_match
        if if_modified_since is not None:
            operation["Headers"]["If-Modified-Since"] = if_modified_since
        if if_none_match is not None:
            operation["Headers"]["If-None-Match"] = if_none_match
        if if_unmodified_since is not None:
            operation["Headers"]["If-Unmodified-Since"] = if_unmodified_since
        if range is not None:
            operation["Headers"]["Range"] = range
        if x_qs_encryption_customer_algorithm is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Algorithm"
                                 ] = x_qs_encryption_customer_algorithm
        if x_qs_encryption_customer_key is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key"
                                 ] = x_qs_encryption_customer_key
        if x_qs_encryption_customer_key_md5 is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key-MD5"
                                 ] = x_qs_encryption_customer_key_md5
        self.get_object_validate(operation)
        return Request(self.config, operation)

    def get_object(
        self,
        object_key,
        response_cache_control=None,
        response_content_disposition=None,
        response_content_encoding=None,
        response_content_language=None,
        response_content_type=None,
        response_expires=None,
        if_match=None,
        if_modified_since=None,
        if_none_match=None,
        if_unmodified_since=None,
        range=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None
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
        if_match=None,
        if_modified_since=None,
        if_none_match=None,
        if_unmodified_since=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None
    ):
        operation = {
            "API": "HeadObject",
            "Method": "HEAD",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {},
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        if if_match is not None:
            operation["Headers"]["If-Match"] = if_match
        if if_modified_since is not None:
            operation["Headers"]["If-Modified-Since"] = if_modified_since
        if if_none_match is not None:
            operation["Headers"]["If-None-Match"] = if_none_match
        if if_unmodified_since is not None:
            operation["Headers"]["If-Unmodified-Since"] = if_unmodified_since
        if x_qs_encryption_customer_algorithm is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Algorithm"
                                 ] = x_qs_encryption_customer_algorithm
        if x_qs_encryption_customer_key is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key"
                                 ] = x_qs_encryption_customer_key
        if x_qs_encryption_customer_key_md5 is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key-MD5"
                                 ] = x_qs_encryption_customer_key_md5
        self.head_object_validate(operation)
        return Request(self.config, operation)

    def head_object(
        self,
        object_key,
        if_match=None,
        if_modified_since=None,
        if_none_match=None,
        if_unmodified_since=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None
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
        action=None,
        response_cache_control=None,
        response_content_disposition=None,
        response_content_encoding=None,
        response_content_language=None,
        response_content_type=None,
        response_expires=None,
        if_modified_since=None
    ):
        operation = {
            "API": "ImageProcess",
            "Method": "GET",
            "URI": "/<bucket-name>/<object-key>?image",
            "Headers": {},
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
        if if_modified_since is not None:
            operation["Headers"]["If-Modified-Since"] = if_modified_since
        self.image_process_validate(operation)
        return Request(self.config, operation)

    def image_process(
        self,
        object_key,
        action=None,
        response_cache_control=None,
        response_content_disposition=None,
        response_content_encoding=None,
        response_content_language=None,
        response_content_type=None,
        response_expires=None,
        if_modified_since=None
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
        if "action" not in op["Params"]:
            raise ParameterRequiredError("action", "ImageProcessInput")
        pass

    def initiate_multipart_upload_request(
        self,
        object_key,
        content_type=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None,
        x_qs_meta_data=None,
        x_qs_storage_class=None
    ):
        operation = {
            "API": "InitiateMultipartUpload",
            "Method": "POST",
            "URI": "/<bucket-name>/<object-key>?uploads",
            "Headers": {},
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        if content_type is not None:
            operation["Headers"]["Content-Type"] = content_type
        if x_qs_encryption_customer_algorithm is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Algorithm"
                                 ] = x_qs_encryption_customer_algorithm
        if x_qs_encryption_customer_key is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key"
                                 ] = x_qs_encryption_customer_key
        if x_qs_encryption_customer_key_md5 is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key-MD5"
                                 ] = x_qs_encryption_customer_key_md5
        if x_qs_meta_data is not None:
            operation["Headers"]["X-QS-MetaData"] = x_qs_meta_data
        if x_qs_storage_class is not None:
            operation["Headers"]["X-QS-Storage-Class"] = x_qs_storage_class
        self.initiate_multipart_upload_validate(operation)
        return Request(self.config, operation)

    def initiate_multipart_upload(
        self,
        object_key,
        content_type=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None,
        x_qs_meta_data=None,
        x_qs_storage_class=None
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
        if "X-QS-Storage-Class" in op["Headers"]:
            x_qs_storage_class_valid_values = ["STANDARD", "STANDARD_IA"]
            if str(op["Headers"]["X-QS-Storage-Class"]
                   ) not in x_qs_storage_class_valid_values:
                raise ParameterValueNotAllowedError(
                    "X-QS-Storage-Class", op["Headers"]["X-QS-Storage-Class"],
                    x_qs_storage_class_valid_values
                )
        pass

    def list_multipart_request(
        self, object_key, limit=None, part_number_marker=None, upload_id=None
    ):
        operation = {
            "API": "ListMultipart",
            "Method": "GET",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {},
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
        self, object_key, limit=None, part_number_marker=None, upload_id=None
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
        if "upload_id" not in op["Params"]:
            raise ParameterRequiredError("upload_id", "ListMultipartInput")
        pass

    def options_object_request(
        self,
        object_key,
        access_control_request_headers=None,
        access_control_request_method=None,
        origin=None
    ):
        operation = {
            "API": "OptionsObject",
            "Method": "OPTIONS",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {},
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": None
        }
        operation["Properties"]["object-key"] = object_key
        if access_control_request_headers is not None:
            operation["Headers"]["Access-Control-Request-Headers"
                                 ] = access_control_request_headers
        if access_control_request_method is not None:
            operation["Headers"]["Access-Control-Request-Method"
                                 ] = access_control_request_method
        if origin is not None:
            operation["Headers"]["Origin"] = origin
        self.options_object_validate(operation)
        return Request(self.config, operation)

    def options_object(
        self,
        object_key,
        access_control_request_headers=None,
        access_control_request_method=None,
        origin=None
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
        if "Access-Control-Request-Method" not in op["Headers"]:
            raise ParameterRequiredError(
                "Access-Control-Request-Method", "OptionsObjectInput"
            )
        if "Origin" not in op["Headers"]:
            raise ParameterRequiredError("Origin", "OptionsObjectInput")
        pass

    def put_object_request(
        self,
        object_key,
        cache_control=None,
        content_encoding=None,
        content_length=None,
        content_md5=None,
        content_type=None,
        expect=None,
        x_qs_copy_source=None,
        x_qs_copy_source_encryption_customer_algorithm=None,
        x_qs_copy_source_encryption_customer_key=None,
        x_qs_copy_source_encryption_customer_key_md5=None,
        x_qs_copy_source_if_match=None,
        x_qs_copy_source_if_modified_since=None,
        x_qs_copy_source_if_none_match=None,
        x_qs_copy_source_if_unmodified_since=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None,
        x_qs_fetch_if_unmodified_since=None,
        x_qs_fetch_source=None,
        x_qs_meta_data=None,
        x_qs_metadata_directive=None,
        x_qs_move_source=None,
        x_qs_storage_class=None,
        body=None
    ):
        operation = {
            "API": "PutObject",
            "Method": "PUT",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {},
            "Params": {},
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": body
        }
        operation["Properties"]["object-key"] = object_key
        if cache_control is not None:
            operation["Headers"]["Cache-Control"] = cache_control
        if content_encoding is not None:
            operation["Headers"]["Content-Encoding"] = content_encoding
        if content_length is not None:
            operation["Headers"]["Content-Length"] = content_length
        if content_md5 is not None:
            operation["Headers"]["Content-MD5"] = content_md5
        if content_type is not None:
            operation["Headers"]["Content-Type"] = content_type
        if expect is not None:
            operation["Headers"]["Expect"] = expect
        if x_qs_copy_source is not None:
            operation["Headers"]["X-QS-Copy-Source"] = x_qs_copy_source
        if x_qs_copy_source_encryption_customer_algorithm is not None:
            operation["Headers"
                      ]["X-QS-Copy-Source-Encryption-Customer-Algorithm"
                        ] = x_qs_copy_source_encryption_customer_algorithm
        if x_qs_copy_source_encryption_customer_key is not None:
            operation["Headers"]["X-QS-Copy-Source-Encryption-Customer-Key"
                                 ] = x_qs_copy_source_encryption_customer_key
        if x_qs_copy_source_encryption_customer_key_md5 is not None:
            operation["Headers"
                      ]["X-QS-Copy-Source-Encryption-Customer-Key-MD5"
                        ] = x_qs_copy_source_encryption_customer_key_md5
        if x_qs_copy_source_if_match is not None:
            operation["Headers"]["X-QS-Copy-Source-If-Match"
                                 ] = x_qs_copy_source_if_match
        if x_qs_copy_source_if_modified_since is not None:
            operation["Headers"]["X-QS-Copy-Source-If-Modified-Since"
                                 ] = x_qs_copy_source_if_modified_since
        if x_qs_copy_source_if_none_match is not None:
            operation["Headers"]["X-QS-Copy-Source-If-None-Match"
                                 ] = x_qs_copy_source_if_none_match
        if x_qs_copy_source_if_unmodified_since is not None:
            operation["Headers"]["X-QS-Copy-Source-If-Unmodified-Since"
                                 ] = x_qs_copy_source_if_unmodified_since
        if x_qs_encryption_customer_algorithm is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Algorithm"
                                 ] = x_qs_encryption_customer_algorithm
        if x_qs_encryption_customer_key is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key"
                                 ] = x_qs_encryption_customer_key
        if x_qs_encryption_customer_key_md5 is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key-MD5"
                                 ] = x_qs_encryption_customer_key_md5
        if x_qs_fetch_if_unmodified_since is not None:
            operation["Headers"]["X-QS-Fetch-If-Unmodified-Since"
                                 ] = x_qs_fetch_if_unmodified_since
        if x_qs_fetch_source is not None:
            operation["Headers"]["X-QS-Fetch-Source"] = x_qs_fetch_source
        if x_qs_meta_data is not None:
            operation["Headers"]["X-QS-MetaData"] = x_qs_meta_data
        if x_qs_metadata_directive is not None:
            operation["Headers"]["X-QS-Metadata-Directive"
                                 ] = x_qs_metadata_directive
        if x_qs_move_source is not None:
            operation["Headers"]["X-QS-Move-Source"] = x_qs_move_source
        if x_qs_storage_class is not None:
            operation["Headers"]["X-QS-Storage-Class"] = x_qs_storage_class
        self.put_object_validate(operation)
        return Request(self.config, operation)

    def put_object(
        self,
        object_key,
        cache_control=None,
        content_encoding=None,
        content_length=None,
        content_md5=None,
        content_type=None,
        expect=None,
        x_qs_copy_source=None,
        x_qs_copy_source_encryption_customer_algorithm=None,
        x_qs_copy_source_encryption_customer_key=None,
        x_qs_copy_source_encryption_customer_key_md5=None,
        x_qs_copy_source_if_match=None,
        x_qs_copy_source_if_modified_since=None,
        x_qs_copy_source_if_none_match=None,
        x_qs_copy_source_if_unmodified_since=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None,
        x_qs_fetch_if_unmodified_since=None,
        x_qs_fetch_source=None,
        x_qs_meta_data=None,
        x_qs_metadata_directive=None,
        x_qs_move_source=None,
        x_qs_storage_class=None,
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
        if "X-QS-Metadata-Directive" in op["Headers"]:
            x_qs_metadata_directive_valid_values = ["COPY", "REPLACE"]
            if str(op["Headers"]["X-QS-Metadata-Directive"]
                   ) not in x_qs_metadata_directive_valid_values:
                raise ParameterValueNotAllowedError(
                    "X-QS-Metadata-Directive",
                    op["Headers"]["X-QS-Metadata-Directive"],
                    x_qs_metadata_directive_valid_values
                )
        if "X-QS-Storage-Class" in op["Headers"]:
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
        upload_id=None,
        content_length=None,
        content_md5=None,
        x_qs_copy_range=None,
        x_qs_copy_source=None,
        x_qs_copy_source_encryption_customer_algorithm=None,
        x_qs_copy_source_encryption_customer_key=None,
        x_qs_copy_source_encryption_customer_key_md5=None,
        x_qs_copy_source_if_match=None,
        x_qs_copy_source_if_modified_since=None,
        x_qs_copy_source_if_none_match=None,
        x_qs_copy_source_if_unmodified_since=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None,
        body=None
    ):
        operation = {
            "API": "UploadMultipart",
            "Method": "PUT",
            "URI": "/<bucket-name>/<object-key>",
            "Headers": {},
            "Params": {
                "part_number": part_number,
                "upload_id": upload_id,
            },
            "Elements": {},
            "Properties": self.properties.copy(),
            "Body": body
        }
        operation["Properties"]["object-key"] = object_key
        if content_length is not None:
            operation["Headers"]["Content-Length"] = content_length
        if content_md5 is not None:
            operation["Headers"]["Content-MD5"] = content_md5
        if x_qs_copy_range is not None:
            operation["Headers"]["X-QS-Copy-Range"] = x_qs_copy_range
        if x_qs_copy_source is not None:
            operation["Headers"]["X-QS-Copy-Source"] = x_qs_copy_source
        if x_qs_copy_source_encryption_customer_algorithm is not None:
            operation["Headers"
                      ]["X-QS-Copy-Source-Encryption-Customer-Algorithm"
                        ] = x_qs_copy_source_encryption_customer_algorithm
        if x_qs_copy_source_encryption_customer_key is not None:
            operation["Headers"]["X-QS-Copy-Source-Encryption-Customer-Key"
                                 ] = x_qs_copy_source_encryption_customer_key
        if x_qs_copy_source_encryption_customer_key_md5 is not None:
            operation["Headers"
                      ]["X-QS-Copy-Source-Encryption-Customer-Key-MD5"
                        ] = x_qs_copy_source_encryption_customer_key_md5
        if x_qs_copy_source_if_match is not None:
            operation["Headers"]["X-QS-Copy-Source-If-Match"
                                 ] = x_qs_copy_source_if_match
        if x_qs_copy_source_if_modified_since is not None:
            operation["Headers"]["X-QS-Copy-Source-If-Modified-Since"
                                 ] = x_qs_copy_source_if_modified_since
        if x_qs_copy_source_if_none_match is not None:
            operation["Headers"]["X-QS-Copy-Source-If-None-Match"
                                 ] = x_qs_copy_source_if_none_match
        if x_qs_copy_source_if_unmodified_since is not None:
            operation["Headers"]["X-QS-Copy-Source-If-Unmodified-Since"
                                 ] = x_qs_copy_source_if_unmodified_since
        if x_qs_encryption_customer_algorithm is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Algorithm"
                                 ] = x_qs_encryption_customer_algorithm
        if x_qs_encryption_customer_key is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key"
                                 ] = x_qs_encryption_customer_key
        if x_qs_encryption_customer_key_md5 is not None:
            operation["Headers"]["X-QS-Encryption-Customer-Key-MD5"
                                 ] = x_qs_encryption_customer_key_md5
        self.upload_multipart_validate(operation)
        return Request(self.config, operation)

    def upload_multipart(
        self,
        object_key,
        part_number=None,
        upload_id=None,
        content_length=None,
        content_md5=None,
        x_qs_copy_range=None,
        x_qs_copy_source=None,
        x_qs_copy_source_encryption_customer_algorithm=None,
        x_qs_copy_source_encryption_customer_key=None,
        x_qs_copy_source_encryption_customer_key_md5=None,
        x_qs_copy_source_if_match=None,
        x_qs_copy_source_if_modified_since=None,
        x_qs_copy_source_if_none_match=None,
        x_qs_copy_source_if_unmodified_since=None,
        x_qs_encryption_customer_algorithm=None,
        x_qs_encryption_customer_key=None,
        x_qs_encryption_customer_key_md5=None,
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
        if "part_number" not in op["Params"]:
            raise ParameterRequiredError("part_number", "UploadMultipartInput")
        if "upload_id" not in op["Params"]:
            raise ParameterRequiredError("upload_id", "UploadMultipartInput")
        pass
