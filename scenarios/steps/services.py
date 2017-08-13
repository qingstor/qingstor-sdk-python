# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from os import path

from assertpy import assert_that
from behave import *

from qingstor.sdk.config import Config
from qingstor.sdk.service.qingstor import QingStor

test_config_file_path = path.abspath(
    path.join(path.dirname(__file__), path.pardir)
)
config = Config(
).load_config_from_filepath(test_config_file_path + "/config.yaml")


@when(u'initialize QingStor service')
def step_impl(context):
    context.qingstor = QingStor(config)


@then(u'the QingStor service is initialized')
def step_impl(context):
    assert_that(context.qingstor).is_not_none()


@when(u'list buckets')
def step_impl(context):
    context.qingstor = QingStor(config)
    context.res = context.qingstor.list_buckets()


@then(u'list buckets status code is 200')
def step_impl(context):
    assert_that(context.res.status_code).is_equal_to(200)
