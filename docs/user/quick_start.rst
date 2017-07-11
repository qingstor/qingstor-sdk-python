Quick Start
===========

Before using qingstor-sdk, please confirm that you already know `QingStor Object Storage basic concepts <https://docs.qingcloud.com/qingstor/api/common/overview.html>`_ , such as  ``Zone``, ``Serivce``, ``Bucket``, ``Object`` and so on.

Preparing Work
--------------

In order to use qingstor-sdk, you need to apply `API Key <https://console.qingcloud.com/access_keys/>`_ first in our console which including ``access_key_id`` and ``secret_access_key``.

``access_key_id`` will be sent as params in every request, and ``secret_access_key`` is used to generate request signature. ``secret_access_key`` need to be properly kept, do not rumor.

Configuration
-------------

Before use qingstor-sdk, we need to create a local configuration. Configuration is placed at ``~/.qingstor/config.yaml`` by default, you can also specify a specific location by calling the ``load_config_from_filepath()`` method when the SDK is initialized.

The configuration file also supports config ``host``, ``port`` and other parameters, you only need to add the corresponding configuration items, all the configurable items are as follows::

    access_key_id: 'ACCESS_KEY_ID_EXAMPLE'
    secret_access_key: 'SECRET_ACCESS_KEY_EXAMPLE'
    host: 'qingstor.com'
    port: 443
    protocol: 'https'
    connection_retries: 3
    # Valid levels are 'debug', 'info', 'warn', 'error', and 'fatal'.
    log_level: 'debug'

Initialize Service
------------------

First we need to initialize a QingStor Service to call services that QingStor provided:

.. code:: python

    from qingstor.sdk.service.qingstor import QingStor
    from qingstor.sdk.config import Config

    config = Config().load_user_config()
    service = QingStor(config)

The object that appear in the above code:

-  ``config`` object carries the user's authentication information and configuration.
-  ``service`` object is used to manipulate the QingStor Object Storage service, you can use it to create a Bucket object or use all service-level APIs.

Create a Bucket
---------------

First we need to initialize a Bucket object to operate on the bucket:

.. code:: python

    bucket = service.Bucket("test", "pek3a")

The object that appear in the above code:

- ``bucket`` object is used to manipulate the bucket and can use all of the bucket and object levels API.

After the object is created, we need to actually create the bucket:

.. code:: python

    resp = bucket.put()
    print(resp.status_code)

The functions that appear in the above code:

- ``bucket.put()`` will create a ``test`` bucket in ``pek3a``

The object that appears in the above code:

- resp object is the response of bucket.put()
- status\_code is a property of the resp object that indicates the status code returned by this operating server. In the result of the request return, the HTTP status code indicates the status of the processing, which conforms to the semantics specified by the HTTP specification.

Get Buckets under accounts
--------------------------

Before we created a Bucket, then we will demonstrate how to get all the Buckets under the account.

.. code:: python

    resp = service.list_buckets()
    print(resp['count'])
    print(resp['buckets'])

The functions that appear in the above code:

-  `service.list\_buckets() <https://docs.qingcloud.com/qingstor/api/service/get.html>`__
   List all the buckets owned by the currently used account.

The object that appear in the above code:

- resp object is the response of bucket.list\_buckets()

    When the response's content-type is ``application-json`` , sdk will attempt to parse the return body and add the individual keys to the resp object. At this point you can manipulate the resp object as a dict. In this example, the contents of the resp object can be referenced at `GET Service <https://docs.qingcloud.com/qingstor/api/service/get.html>`_.

Upload an Object
----------------

Next we will show you how to upload an Object in the Bucket:

.. code:: python

    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        resp = bucket.put_object(
            'example_key', body=f
        )

    print(resp.status_code)

The functions that appear in the above code:

-  tempfile.NamedTemporaryFile() created a temporary file.
-  `bucket.put\_object() <https://docs.qingcloud.com/qingstor/api/object/put.html>`_
   Upload an Object to Bucket.
  -  The first argument represents the Key of the Object, and the Object Key is the identity of the object that corresponds to the bucket in the QingStor object storage system, which is equivalent to the file name in the local storage system.
  -  ``body`` means the contents of the upload Object, it's value can be a string ans also can be any file object.

List Objects in Bucket
----------------------

Before we upload an Object in Bucket, we will show you how to list objects in Bucket:

.. code:: python

    resp = bucket.list_objects()
    print(resp['keys'])

The functions that appear in the above code:

-  `bucket.list\_objects() <https://docs.qingcloud.com/qingstor/api/bucket/get.html>`_
   List objects in the bucket.

Download an Object
------------------

.. code:: python

    import tempfile
    resp = bucket.get_object('example_key')
    with tempfile.NamedTemporaryFile() as f:
        for chunk in resp.iter_content():
            f.write(chunk)

The functions that appear in the above code:

-  tempfile.NamedTemporaryFile() created a temporary file.
-  `bucket.get\_object() <https://docs.qingcloud.com/qingstor/api/object/get.html>`_
   Get an Object.
-  ``resp.iter_content()`` Automatically iterates the contents of an Object to reduce memory footprint and improve performance

Check the status of an Object
-----------------------------

.. code:: python

    resp = bucket.head_object('example_key')
    print(resp.status_code)

The functions that appear in the above code:

-  `bucket.head\_object() <https://docs.qingcloud.com/qingstor/api/object/head.html>`__
   View the status of an Object, the returning object's status\_code conforms to the semantics specified by the HTTP specification. For example: 200 means the file status is normal, you can download or delete it; 404 means the file does not exist and so on.

Delete an Object
----------------

Next we will show you how to delete an object.

.. code:: python

    resp = bucket.delete_object('example_key')
    print(resp.status_code)

The functions that appear in the above code:

-  `bucket.delete\_object() <https://docs.qingcloud.com/qingstor/api/object/delete.html>`__
   Delete an Object.

Initialize a multipart upload
-----------------------------

QingStor Object Storage support for file multipart upload, maximum support 10,000, each size up to 5G, on the one hand to help users to large files in the shortest possible time to upload, on the other hand allows users to store up to 50TB file.
Below we will show how to use the QingStor Object Storage Multipart Upload API.

.. code:: python

    resp = bucket.initiate_multipart_upload('example_upload_key')
    example_upload_id = resp['upload_id']
    print(resp.status_code)

The functions that appear in the above code:

-  `bucket.initiate\_multipart\_upload() <https://docs.qingcloud.com/qingstor/api/object/multipart/initiate_multipart_upload.html>`_
   Initialize a segment upload, the request will return a Upload ID. When uploading a segment, the Upload ID is appended to the request parameter, indicating that the segment belongs to the same object.

Upload a multipart
------------------

.. code:: python

    import tempfile
    with tempfile.NamedTemporaryFile() as f:
        f.seek(1024*1024*5)
        f.write('\0'.encode())
        f.flush()
        f.seek(0)
        resp = bucket.upload_multipart(
            'example_upload_key',
            upload_id=example_upload_id,
            part_number=0,
            body=f
        )

The functions that appear in the above code:

-  tempfile.NamedTemporaryFile(), f.seek(), f.write(), f.flush()
   Created a temporary file with a size of 5MB
-  `bucket.upload\_multipart() <https://docs.qingcloud.com/qingstor/api/object/multipart/upload_multipart.html>`_
   Used to upload a multipart. Except the last segment, the other segments have a minimum size of 4M and a maximum size  of 1G.
-  ``upload_id`` is the returning ``Upload ID`` while initiate_multipart_upload, multipart upload with the same ``Upload ID`` means they belong to the same object.
-  ``part_number`` is part number, parts merged in accordance with the part number from small to large order.

List multipart uploaded
-----------------------

.. code:: python

    resp = bucket.list_multipart(
        'example_upload_key',
        upload_id=example_upload_id
    )
    example_object_parts = resp.object_parts
    print(resp['count'])

The functions that appear in the above code:

-  `bucket.list\_multipart() <https://docs.qingcloud.com/qingstor/api/object/multipart/list_multipart.html>`_
   Used to list multiparts that have been uploaded.

Complete a multipart upload
---------------------------

.. code:: python

    resp = bucket.complete_multipart_upload(
        'example_upload_key',
        upload_id=example_upload_id,
        object_parts=example_object_parts
    )
    print(resp.status_code)

The functions that appear in the above code:

-  `bucket.complete\_multipart\_upload() <https://docs.qingcloud.com/qingstor/api/object/multipart/complete_multipart_upload.html>`_
   Used to end this multipart upload, to get a complete object. When this API is not called, the multipart upload is in an incomplete state, and the GET request to retrieve the object will return an error.
-  ``object_parts`` specify the part number that needed to merge, should follow the part number from small to large order.

Abort a multipart upload
------------------------

.. code:: python

    resp = bucket.abort_multipart_upload(
        'example_upload_key',
        upload_id=example_upload_id
    )
    print(resp.status_code)

The functions that appear in the above code:

-  `bucket.abort\_multipart\_upload() <https://docs.qingcloud.com/qingstor/api/object/multipart/abort_multipart_upload.html>`_
   Terminate the multipart upload, and delete the already uploaded multipart.

Get bucket's access control list
--------------------------------

The QingStor Object Storage support storage access control lists (Bucket ACLs). For storage-level access control, users can grant read, write, read, or read and write permissions to a single or multiple QingCloud users. Here we will demonstrate how to use the API to get and set the Bucket ACL.

.. code:: python

    resp = bucket.get_acl()
    print(resp['acl'])

The functions that appear in the above code:

-  `bucket.get\_acl() <https://docs.qingcloud.com/qingstor/api/bucket/acl/get_acl.html>`_
   Get access control list for Bucket.

Set bucket's access control list
--------------------------------

.. code:: python

    example_acl = [
        {
            "grantee": {
                "type": "group",
                "name": "QS_ALL_USERS"
            },
            "permission": "READ"
        }
    ]
    resp = bucket.put_acl(
        acl=example_acl
    )
    print(resp.status_code)

The functions that appear in the above code:

-  `bucket.put\_acl() <https://docs.qingcloud.com/qingstor/api/bucket/acl/put_acl.html>`__
   Set access control list for Bucket.
-  ``acl`` used to set Bucket's ACL. This example gives all QingCloud users the read access to the bucket

More operations
---------------

All API call interfaces are similar to the example above, you can visit `QingStor Object Storage API Documentation <https://docs.qingcloud.com/qingstor/api/index.html>`_ for more information.
