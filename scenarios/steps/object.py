# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import time
from os import path
from os import system

import requests
import yaml
from assertpy import assert_that
from behave import *

from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import QingStor

test_config_file_path = path.abspath(
    path.join(path.dirname(__file__), path.pardir)
)
config = Config().load_config_from_filepath(test_config_file_path + "/config.yaml")
qingstor = QingStor(config)
with open(test_config_file_path + '/test_config.yaml') as f:
    test = yaml.load(f)
    f.close()
bucket = qingstor.Bucket(test['bucket_name'], test['zone'])
bucket.put()


@when(u'put object with key "{key}"')
def step_impl(context, key):
    system('dd if=/dev/zero of=/tmp/sdk_bin bs=1048576 count=1')
    with open('/tmp/sdk_bin') as f:
        context.res = bucket.put_object(key, body=f)


@then(u'put object status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'copy object with key "{key}"')
def step_impl(context, key):
    context.res = bucket.put_object(
        key + 'copy',
        x_qs_copy_source=''.join(['/', test['bucket_name'], '/', key])
    )


@then(u'copy object status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'move object with key "{key}"')
def step_impl(context, key):
    context.res = bucket.put_object(
        key + 'move',
        x_qs_move_source=''.join(['/', test['bucket_name'], '/', key + 'copy'])
    )


@then(u'move object status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'get object with key "{key}"')
def step_impl(context, key):
    context.res = bucket.get_object(key)


@then(u'get object status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@then(u'get object content length is 1048576')
def step_impl(context):
    assert_that(len(context.res.content)).is_equal_to(1048576)


@when(u'get object "{key}" with query signature')
def step_impl(context, key):
    expires = int(time.time()) + 100
    req = bucket.get_object_request(key).sign_query(expires)
    context.res = requests.session().send(req)


@then(u'get object with query signature content length is 1048576')
def step_impl(context):
    assert_that(len(context.res.content)).is_equal_to(1048576)


@when(u'get object "{key}" with content type "video/mp4; charset=utf8"')
def step_impl(context, key):
    context.res = bucket.get_object(
        key, response_content_type='video/mp4; charset=utf8'
    )


@then(u'get object content type is "video/mp4; charset=utf8"')
def step_impl(context):
    assert_that(context.res.headers['Content-Type'], 'video/mp4; charset=utf8')


@when(u'head object with key "{key}"')
def step_impl(context, key):
    context.res = bucket.head_object(key)


@then(u'head object status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'options object "{key}" with method "GET" and origin "qingcloud.com"')
def step_impl(context, key):
    context.res = bucket.options_object(
        key, access_control_request_method='GET', origin='qingcloud.com'
    )


@then(u'options object status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'delete object with key "{key}"')
def step_impl(context, key):
    context.res = bucket.delete_object(key)


@then(u'delete object status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)


@when(u'delete the move object with key "{key}"')
def step_impl(context, key):
    context.res = bucket.delete_object(key + 'move')


@then(u'delete the move object status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)
