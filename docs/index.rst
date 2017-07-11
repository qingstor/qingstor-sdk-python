qingstor-sdk: SDK for QingStor
==============================

Release v\ |version|. (:ref:`Installation <install>`)

.. image:: https://travis-ci.org/yunify/qingstor-sdk-python.svg?branch=master
    :target: https://travis-ci.org/yunify/qingstor-sdk-python

.. image:: http://img.shields.io/badge/api-reference-green.svg
    :target: https://docs.qingcloud.com/qingstor/

.. image:: http://img.shields.io/badge/license-apache%20v2-blue.svg
    :target: https://github.com/yunify/qingstor-sdk-python/blob/master/LICENSE

**qingstor-sdk** is the official QingStor SDK for the Python programming language, compatible with Python 2.6, 2.7 and 3.4+ versions.

.. code:: python

    >>> from qingstor.sdk.service.qingstor import QingStor
    >>> from qingstor.sdk.config import Config
    >>> config = Config('ACCESS_KEY_ID_EXAMPLE', 'SECRET_ACCESS_KEY_EXAMPLE')
    >>> qingstor = QingStor(config)
    >>> r = qingstor.list_buckets()
    >>> r.status_code
    200
    >>> r['count']
    7
    >>> r['buckets'][0]['name']
    'python-sdk-test'
    >>> r.headers['content-type']
    'application/json'
    >>> r.content
    b'{"count": 7, "buckets":...

User Guide
----------

This part of the documentation, which is mostly prose, begins with some background information about qingstor-sdk, then focuses on step-by-step instructions for getting the most out of qingstor-sdk.

.. toctree::
   :maxdepth: 2

   user/quick_start

Config Documentation
--------------------

If you are looking for information on config, this part of the documentation is
for you.

.. toctree::
   :maxdepth: 2

   configuration

API Documentation
-----------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api
