.. _configuration:

Configuration Guide
===================

Summary
-------

This SDK uses a class called "Config" to store and manage configuration,
read comments of public functions in
`"config.py" <https://github.com/yunify/qingstor-sdk-python/blob/master/config.py>`__
for details.

Except for Access Key, you can also configure the API endpoint for
private cloud usage scenario. All available configurable items are
listed in the default configuration file.

**Default Configuration File:**

.. code:: yaml

    # QingStor services configuration

    access_key_id: ''
    secret_access_key: ''

    host: 'qingstor.com'
    port: 443
    protocol: 'https'
    connection_retries: 3

    # Valid log levels are "debug", "info", "warn", "error", and "fatal".
    log_level: 'warn'

Usage
-----

Just create a config structure instance with your API Access Key, and
initialize services.

Code Snippet
~~~~~~~~~~~~

Create default configuration

.. code:: python

    default_config = Config()

Create configuration from Access Key

.. code:: python

    configuration = Config('ACCESS_KEY_ID', 'SECRET_ACCESS_KEY')

    another_configuration = Config()
    another_configuration.access_key_id = "ACCESS_KEY_ID"
    another_configuration.secret_access_key = "SECRET_ACCESS_KEY"

Load user configuration

.. code:: python

    user_config = Config().load_user_config()

Load configuration from config file

.. code:: python

    config_from_file = Config().load_config_from_filepath('PATH/TO/FILE')

Change API endpoint

.. code:: python

    more_configuration = Config()

    more_configuration.protocol = 'https'
    more_configuration.host = 'api.private.com'
    more_configuration.port = 4433
