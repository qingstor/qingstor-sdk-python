# -*- coding: utf-8 -*-

import json
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


@when(u'put bucket policy')
def step_impl(context):
    data = json.loads(context.text)
    if data['statement']:
        data['statement'][0]['resource'] = [test['bucket_name'] + '/*']
    context.res = bucket.put_policy(data['statement'])


@then(u'put bucket policy status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'get bucket policy')
def step_impl(context):
    context.res = bucket.get_policy()


@then(u'get bucket policy status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@then(u'get bucket policy should have Referer "*.example1.com"')
def step_impl(context):
    ok = False
    for statement in context.res['statement']:
        for i in statement['condition']['string_like']['Referer']:
            if i == '*.example1.com':
                ok = True
    assert_that(ok).is_equal_to(True)


@when(u'delete bucket policy')
def step_impl(context):
    context.res = bucket.delete_policy()


@then(u'delete bucket policy status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)
