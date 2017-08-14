# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from os import path

import yaml
from assertpy import assert_that
from behave import *

from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import QingStor

test_config_file_path = path.abspath(
    path.join(path.dirname(__file__), path.pardir)
)
config = Config(
).load_config_from_filepath(test_config_file_path + "/config.yaml")
qingstor = QingStor(config)
with open(test_config_file_path + '/test_config.yaml') as f:
    test = yaml.load(f)
    f.close()
bucket = qingstor.Bucket(test['bucket_name'], test['zone'])
bucket.put()


@when(u'initialize the bucket')
def step_impl(context):
    context.bucket = qingstor.Bucket(test['bucket_name'], test['zone'])


@then(u'the bucket is initialized')
def step_impl(context):
    assert_that(context.bucket).is_not_none()


@when(u'put bucket')
def step_impl(context):
    pass


@then(u'put bucket status code is 201')
def step_impl(context):
    pass


@when(u'put same bucket again')
def step_impl(context):
    context.res = bucket.put()


@then(u'put same bucket again status code is 409')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(409)


@when(u'list objects')
def step_impl(context):
    context.res = bucket.list_objects()


@then(u'list objects status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@then(u'list objects keys count is 0')
def step_impl(context):
    assert_that(len(context.res['keys'])).is_greater_than_or_equal_to(0)


@when(u'head bucket')
def step_impl(context):
    context.res = bucket.head()


@then(u'head bucket status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'delete multiple objects')
def step_impl(context):
    bucket.put_object('object_0')
    bucket.put_object('object_1')
    bucket.put_object('object_2')
    context.res = bucket.delete_multiple_objects(
        objects=[{
            'key': 'object_0'
        }, {
            'key': 'object_1'
        }, {
            'key': 'object_2'
        }]
    )


@then(u'delete multiple objects code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'get bucket statistics')
def step_impl(context):
    context.res = bucket.get_statistics()


@then(u'get bucket statistics status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@then(u'get bucket statistics status is "active"')
def step_impl(context):
    assert_that(context.res['status']).is_equal_to('active')


@when(u'delete bucket')
def step_impl(context):
    pass


@then(u'delete bucket status code is 204')
def step_impl(context):
    pass


@given(u'an object created by initiate multipart upload')
def step_impl(context):
    context.init_resp = bucket.initiate_multipart_upload(
        "list_multipart_uploads"
    )


@when(u'list multipart uploads')
def step_impl(context):
    context.res = bucket.list_multipart_uploads()


@then(u'list multipart uploads count is 1')
def step_impl(context):
    assert_that(len(context.res["uploads"])).is_equal_to(1)


@when(u'list multipart uploads with prefix')
def step_impl(context):
    context.res = bucket.list_multipart_uploads(prefix="list_multipart_uploads")


@then(u'list multipart uploads with prefix count is 1')
def step_impl(context):
    bucket.abort_multipart_upload(
        "list_multipart_uploads", context.init_resp["upload_id"]
    )
    assert_that(len(context.res["uploads"])).is_equal_to(1)
