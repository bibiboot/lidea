==========================
Lidea
==========================

Ideas for space in this forsaken world around us. Very narcissistic in nature. 

Implementations
================

Includes an auto suggest integerated with osm maps. Convert the osm map to django models level.

Notes
-----




Set-up
-----

1. Install the ``postgresql-9.1``.

2. Create a database named ``osm``.

On Django < 1.3::

    CACHE_BACKEND = 'redis_cache.cache://<host>:<port>'

On Django >= 1.3::


    # When using TCP connections
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '<host>:<port>',
            'OPTIONS': {
                'DB': 1,
                'PASSWORD': 'yadayada',
                'PARSER_CLASS': 'redis.connection.HiredisParser'
            },
        },
    }

    # When using unix domain sockets
    # Note: ``LOCATION`` needs to be the same as the ``unixsocket`` setting
    # in your redis.conf
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '/path/to/socket/file',
            'OPTIONS': {
                'DB': 1,
                'PASSWORD': 'yadayada',
                'PARSER_CLASS': 'redis.connection.HiredisParser'
            },
        },
    }

.. _redis-py: http://github.com/andymccurdy/redis-py/
