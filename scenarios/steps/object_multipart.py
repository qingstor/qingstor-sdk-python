# -*- coding: utf-8 -*-

from os import path
from os import system

import yaml
from assertpy import assert_that
from behave import *

from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import QingStor

config = Config().load_user_config()
qingstor = QingStor(config)
test_config_file_path = path.abspath(
    path.join(path.dirname(__file__), path.pardir))
with open(test_config_file_path + '/test_config.yaml') as f:
    test = yaml.load(f)
    f.close()
bucket = qingstor.Bucket(test['bucket_name'], test['zone'])
bucket.put()
init_multipart_res = None
list_multipart_res = None


@when(u'initiate multipart upload with key "test_object_multipart"')
def step_impl(context):
    global init_multipart_res
    init_multipart_res = bucket.initiate_multipart_upload(
        'test_object_multipart')


@then(u'initiate multipart upload status code is 200')
def step_impl(context):
    assert_that(init_multipart_res.status_code).is_equal_to(200)


@when(u'upload the first part')
def step_impl(context):
    system('dd if=/dev/zero of=/tmp/sdk_bin_part_0 bs=1048576 count=5')
    with open('/tmp/sdk_bin_part_0') as f:
        context.res = bucket.upload_multipart(
            'test_object_multipart', 0, init_multipart_res['upload_id'], body=f)
        f.close()


@then(u'upload the first part status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'upload the second part')
def step_impl(context):
    system('dd if=/dev/zero of=/tmp/sdk_bin_part_1 bs=1048576 count=5')
    with open('/tmp/sdk_bin_part_1') as f:
        context.res = bucket.upload_multipart(
            'test_object_multipart', 1, init_multipart_res['upload_id'], body=f)
        f.close()


@then(u'upload the second part status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'upload the third part')
def step_impl(context):
    system('dd if=/dev/zero of=/tmp/sdk_bin_part_2 bs=1048576 count=5')
    with open('/tmp/sdk_bin_part_2') as f:
        context.res = bucket.upload_multipart(
            'test_object_multipart', 2, init_multipart_res['upload_id'], body=f)
        f.close()


@then(u'upload the third part status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'list multipart')
def step_impl(context):
    global list_multipart_res
    list_multipart_res = bucket.list_multipart(
        'test_object_multipart', upload_id=init_multipart_res['upload_id'])


@then(u'list multipart status code is 200')
def step_impl(context):
    assert_that(list_multipart_res.status_code).is_equal_to(200)


@then(u'list multipart object parts count is 3')
def step_impl(context):
    assert_that(list_multipart_res['count']).is_equal_to(3)


@when(u'complete multipart upload')
def step_impl(context):
    context.res = bucket.complete_multipart_upload(
        'test_object_multipart',
        upload_id=init_multipart_res['upload_id'],
        etag='"4072783b8efb99a9e5817067d68f61c6"',
        object_parts=list_multipart_res['object_parts'])


@then(u'complete multipart upload status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'abort multipart upload')
def step_impl(context):
    context.res = bucket.abort_multipart_upload(
        'test_object_multipart', upload_id=init_multipart_res['upload_id'])


@then(u'abort multipart upload status code is 400')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(400)


@when(u'delete the multipart object')
def step_impl(context):
    context.res = bucket.delete_object('test_object_multipart')


@then(u'delete the multipart object status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)
