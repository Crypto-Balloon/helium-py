Usage
=====

.. _installation:

Installation
------------

To use helium-py, first install it using pip:

.. code-block:: console

   (venv) $ pip install helium-py

Using the helium API
--------------------

To do stuff with the API, take ``helium_py.Cities``:

The `all()` method on an API class returns a generator
that can be used to iterate through all objects returned
by the helium API.

For example:

>>> from helium_py.api import Cities
>>> next(Cities().all(search='Chattanooga'))
{'short_state': 'TN',
 'short_country': 'US',
 'short_city': 'Chattanooga',
 'online_count': 143,
 'offline_count': 27,
 'long_state': 'Tennessee',
 'long_country': 'United States',
 'long_city': 'Chattanooga',
 'hotspot_count': 170,
 'city_id': 'Y2hhdHRhbm9vZ2F0ZW5uZXNzZWV1bml0ZWQgc3RhdGVz'}
