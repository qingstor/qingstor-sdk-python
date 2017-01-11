# -*- coding: utf-8 -*-

import time
from os import path
from os import system

import requests
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


@when(u'put object with key "test_object"')
def step_impl(context):
    system('dd if=/dev/zero of=/tmp/sdk_bin bs=1048576 count=1')
    with open('/tmp/sdk_bin') as f:
        context.res1 = bucket.put_object('test_object', body=f)
    with open('/tmp/sdk_bin') as f:
        context.res2 = bucket.put_object('test_object_string', body=f.read())
    with open('/tmp/sdk_bin') as f:
        context.res3 = bucket.put_object('中文测试', body=f)


@then(u'put object status code is 201')
def step_impl(context):
    assert_that(context.res1.status_code).is_equal_to(201)
    assert_that(context.res2.status_code).is_equal_to(201)
    assert_that(context.res3.status_code).is_equal_to(201)


@when(u'copy object with key "test_object_copy"')
def step_impl(context):
    context.res = bucket.put_object(
        'test_object_copy',
        x_qs_copy_source=''.join(['/', test['bucket_name'], '/', 'test_object'])
    )


@then(u'copy object status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'move object with key "test_object_move"')
def step_impl(context):
    context.res = bucket.put_object(
        'test_object_move',
        x_qs_move_source=''.join(
            ['/', test['bucket_name'], '/', 'test_object_copy']
        )
    )


@then(u'move object status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'get object')
def step_impl(context):
    context.res = bucket.get_object('test_object')


@then(u'get object status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@then(u'get object content length is 1048576')
def step_impl(context):
    assert_that(len(context.res.content)).is_equal_to(1048576)


@when(u'get object with query signature')
def step_impl(context):
    expires = int(time.time()) + 100
    req = bucket.get_object_request('test_object').sign_query(expires)
    context.res = requests.session().send(req)


@then(u'get object with query signature content length is 1048576')
def step_impl(context):
    assert_that(len(context.res.content)).is_equal_to(1048576)


@when(u'get object with content type "video/mp4; charset=utf8"')
def step_impl(context):
    context.res = bucket.get_object(
        'test_object', response_content_type='video/mp4; charset=utf8'
    )


@then(u'get object content type is "video/mp4; charset=utf8"')
def step_impl(context):
    assert_that(context.res.headers['Content-Type'], 'video/mp4; charset=utf8')


@when(u'head object')
def step_impl(context):
    context.res = bucket.head_object('test_object')


@then(u'head object status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'options object with method "GET" and origin "qingcloud.com"')
def step_impl(context):
    context.res = bucket.options_object(
        'test_object',
        access_control_request_method='GET',
        origin='qingcloud.com'
    )


@then(u'options object status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'delete object')
def step_impl(context):
    context.res1 = bucket.delete_object('test_object')
    context.res2 = bucket.delete_object('test_object_string')
    context.res3 = bucket.delete_object('中文测试')


@then(u'delete object status code is 204')
def step_impl(context):
    assert_that(context.res1.status_code).is_equal_to(204)
    assert_that(context.res2.status_code).is_equal_to(204)
    assert_that(context.res3.status_code).is_equal_to(204)


@when(u'delete the move object')
def step_impl(context):
    context.res = bucket.delete_object('test_object_move')


@then(u'delete the move object status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)
