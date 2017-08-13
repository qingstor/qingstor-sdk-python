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


@when(u'put bucket external mirror')
def step_impl(context):
    data = json.loads(context.text)
    context.res = bucket.put_external_mirror(data['source_site'])


@then(u'put bucket external mirror status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@when(u'get bucket external mirror')
def step_impl(context):
    context.res = bucket.get_external_mirror()


@then(u'get bucket external mirror status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)


@then(
    u'get bucket external mirror should have source_site "https://example.com/something/"'
)
def step_impl(context):
    assert_that(context.res['source_site']
                ).is_equal_to('https://example.com/something/')


@when(u'delete bucket external mirror')
def step_impl(context):
    context.res = bucket.delete_external_mirror()


@then(u'delete bucket external mirror status code is 204')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(204)
