==========================
Lidea
==========================

Ideas for space in this forsaken world around us. Very narcissistic in nature. 

Implementations
================

Includes an auto suggest integerated with osm maps. Convert the osm map to django models level.

Set up the postgresql for 'OSM'
-----

1. Install the ``postgresql-9.1``::

    sudo apt-get install postgresql-9.1-postgis postgresql-contrib-9.1

2. Create a database named ``osm``::
    
    sudo -u postgres

3. Run the commands for setting up the geometric function in postgresql::
    
    psql -h HOST -U USERNAME -d DATABASE -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
    psql -h HOST -U USERNAME -d DATABASE -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql

4. Install ``osm2pgsql``.

5. Run the command to transfer data from the osm file to postgresql database::

    osm2pgsql -l -p osm -d DATABASE -U USERNAE -H Host -W OSM_FILE

6. Install ``postgresql_psycopg2``.


Set up the mysql for 'idea'
-----

1. Run the command for creating the mysql databases::

    python manage.py syncdb

2. Fill the with content from the osm, by the command::

    python places/filler.py


Set up the redis for auto suggest
-----

1. Install the `redis`_.

2. Install the `redis-py`_.

3. Run the command to fill the redis with prefixes::

    python suggest/filler.py


Set up the crawler for app 'event'
-----

1. Install the `webkit-server`_.

2. Install the `dryscrape`_.

.. _redis-py: http://github.com/andymccurdy/redis-py/
.. _redis: http://redis.io/download
.. _dryscrape: https://github.com/niklasb/dryscrape
.. _webkit-server: https://github.com/niklasb/webkit-server
