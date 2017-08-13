# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from os import path
from os import system

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
init_multipart_res = None
list_multipart_res = None


@when(u'initiate multipart upload with key "{key}"')
def step_impl(context, key):
    global init_multipart_res
    init_multipart_res = bucket.initiate_multipart_upload(key)


@then(u'initiate multipart upload status code is 200')
def step_impl(context):
    assert_that(init_multipart_res.status_code).is_equal_to(200)


@when(u'upload the first part with key "{key}"')
def step_impl(context, key):
    system('dd if=/dev/zero of=/tmp/sdk_bin_part_0 bs=1048576 count=5')
    with open('/tmp/sdk_bin_part_0') as f:
        context.res = bucket.upload_multipart(
            key, 0, init_multipart_res['upload_id'], body=f
        )
        f.close()


@then(u'upload the first part status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'upload the second part with key "{key}"')
def step_impl(context, key):
    system('dd if=/dev/zero of=/tmp/sdk_bin_part_1 bs=1048576 count=5')
    with open('/tmp/sdk_bin_part_1') as f:
        context.res = bucket.upload_multipart(
            key, 1, init_multipart_res['upload_id'], body=f
        )
        f.close()


@then(u'upload the second part status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'upload the third part with key "{key}"')
def step_impl(context, key):
    system('dd if=/dev/zero of=/tmp/sdk_bin_part_2 bs=1048576 count=5')
    with open('/tmp/sdk_bin_part_2') as f:
        context.res = bucket.upload_multipart(
            key, 2, init_multipart_res['upload_id'], body=f
        )
        f.close()


@then(u'upload the third part status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'list multipart with key "{key}"')
def step_impl(context, key):
    global list_multipart_res
    list_multipart_res = bucket.list_multipart(
        key, upload_id=init_multipart_res['upload_id']
    )


@then(u'list multipart status code is 200')
def step_impl(context):
    assert_that(list_multipart_res.status_code).is_equal_to(200)


@then(u'list multipart object parts count is 3')
def step_impl(context):
    assert_that(list_multipart_res['count']).is_equal_to(3)


@when(u'complete multipart upload with key "{key}"')
def step_impl(context, key):
    context.res = bucket.complete_multipart_upload(
        key,
        upload_id=init_multipart_res['upload_id'],
        etag='"4072783b8efb99a9e5817067d68f61c6"',
        object_parts=list_multipart_res['object_parts']
    )


@then(u'complete multipart upload status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'abort multipart upload with key "{key}"')
def step_impl(context, key):
    context.res = bucket.abort_multipart_upload(
        key, upload_id=init_multipart_res['upload_id']
    )


@then(u'abort multipart upload status code is 400')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(400)


@when(u'delete the multipart object with key "{key}"')
def step_impl(context, key):
    context.res = bucket.delete_object(key)


@then(u'delete the multipart object status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)
