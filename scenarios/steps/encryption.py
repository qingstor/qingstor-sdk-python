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


@when(
    u'put encryption object "{key}" with "{encryption_algorithm}", "{encryption_key}", "{encryption_key_md5}"'
)
def step_impl(
    context, key, encryption_algorithm, encryption_key, encryption_key_md5
):
    system('dd if=/dev/zero of=/tmp/sdk_bin bs=1048576 count=1')
    with open('/tmp/sdk_bin') as f:
        context.res = bucket.put_object(
            key,
            x_qs_encryption_customer_algorithm=encryption_algorithm,
            x_qs_encryption_customer_key=encryption_key,
            x_qs_encryption_customer_key_md5=encryption_key_md5,
            body=f
        )


@then(u'put encryption object status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(
    u'copy encryption object "{key}" with "{encryption_algorithm}", "{encryption_key}", "{encryption_key_md5}"'
)
def step_impl(
    context, key, encryption_algorithm, encryption_key, encryption_key_md5
):
    context.res = bucket.put_object(
        key + 'copy',
        x_qs_copy_source_encryption_customer_algorithm=encryption_algorithm,
        x_qs_copy_source_encryption_customer_key=encryption_key,
        x_qs_copy_source_encryption_customer_key_md5=encryption_key_md5,
        x_qs_copy_source=''.join(['/', test['bucket_name'], '/', key])
    )


@then(u'copy encryption object status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(u'move encryption object with key "{key}"')
def step_impl(context, key):
    context.res = bucket.put_object(
        key + 'move',
        x_qs_move_source=''.join(['/', test['bucket_name'], '/', key + 'copy'])
    )


@then(u'move encryption object status code is 201')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(201)


@when(
    u'get encryption object "{key}" with "{encryption_algorithm}", "{encryption_key}", "{encryption_key_md5}"'
)
def step_impl(
    context, key, encryption_algorithm, encryption_key, encryption_key_md5
):
    context.res = bucket.get_object(
        key,
        x_qs_encryption_customer_algorithm=encryption_algorithm,
        x_qs_encryption_customer_key=encryption_key,
        x_qs_encryption_customer_key_md5=encryption_key_md5
    )


@then(u'get encryption object status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@then(u'get encryption object content length is 1048576')
def step_impl(context):
    assert_that(len(context.res.content)).is_equal_to(1048576)


@when(
    u'head encryption object with key "{key}" with "{encryption_algorithm}", "{encryption_key}", "{encryption_key_md5}"'
)
def step_impl(
    context, key, encryption_algorithm, encryption_key, encryption_key_md5
):
    context.res = bucket.head_object(
        key,
        x_qs_encryption_customer_algorithm=encryption_algorithm,
        x_qs_encryption_customer_key=encryption_key,
        x_qs_encryption_customer_key_md5=encryption_key_md5
    )


@then(u'head encryption object status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'delete encryption object "{key}"')
def step_impl(context, key):
    context.res = bucket.delete_object(key)


@then(u'delete encryption object status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)


@when(u'delete encryption the move object "{key}"')
def step_impl(context, key):
    context.res = bucket.delete_object(key + 'move')


@then(u'delete encryption the move object status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)
