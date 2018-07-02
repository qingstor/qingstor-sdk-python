# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
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


@when(u'put bucket notification')
def step_impl(context):
    data = json.loads(context.text)
    context.res = bucket.put_notification(data['notifications'])


@then(u'put bucket notification status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'get bucket notification')
def step_impl(context):
    context.res = bucket.get_notification()


@then(u'get bucket notification status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@then(u'get bucket notification should have cloudfunc "tupu-porn"')
def step_impl(context):
    ok = False
    for i in context.res['notifications']:
        if i['cloudfunc'] == 'tupu-porn':
            ok = True
    assert_that(ok).is_equal_to(True)


@when(u'delete bucket notification')
def step_impl(context):
    context.res = bucket.delete_notification()


@then(u'delete bucket notification status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)
