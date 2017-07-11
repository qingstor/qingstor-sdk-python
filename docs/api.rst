.. _api:

Developer Interface
===================

.. module:: qingstor.sdk

This part of the documentation covers all the interfaces of qingstor-sdk.

Main Interface
--------------

All of QingStor' functionality can be accessed by these methods.

QingStor Service API
^^^^^^^^^^^^^^^^^^^^

.. automodule:: qingstor.sdk.service.qingstor
        :members:
        :undoc-members:
        :show-inheritance:

QingStor Bucket and Object API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automodule:: qingstor.sdk.service.bucket
        :members:
        :undoc-members:
        :show-inheritance:

Lower-Level Classes
-------------------

Build Class
^^^^^^^^^^^

.. automodule:: qingstor.sdk.build
        :members:
        :undoc-members:
        :show-inheritance:

Request Class
^^^^^^^^^^^^^

.. automodule:: qingstor.sdk.request
        :members:
        :undoc-members:
        :show-inheritance:

Unpack Class
^^^^^^^^^^^^

.. automodule:: qingstor.sdk.unpac
        :members:
        :undoc-members:
        :show-inheritance:

Config Class
^^^^^^^^^^^^

.. automodule:: qingstor.sdk.config
        :members:
        :undoc-members:
        :show-inheritance:

Exceptions
----------

.. autoexception:: qingstor.sdk.error.ParameterRequiredError
.. autoexception:: qingstor.sdk.error.ParameterValueNotAllowedError
