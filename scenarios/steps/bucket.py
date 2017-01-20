# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from os import path

import yaml
from assertpy import assert_that
from behave import *

from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import QingStor

config = Config().load_user_config()
qingstor = QingStor(config)
test_config_file_path = path.abspath(
    path.join(path.dirname(__file__), path.pardir)
)
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
    another_bucket = qingstor.Bucket(test['bucket_name'] + '1', test['zone'])
    context.res = another_bucket.put()


@then(u'put bucket status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


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
    assert_that(len(context.res['keys'])).is_equal_to(0)


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
    another_bucket = qingstor.Bucket(test['bucket_name'] + '1', test['zone'])
    context.res = another_bucket.delete()
    print(context.res.content)


@then(u'delete bucket status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)
