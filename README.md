lidea
=====

Ideas for space in this forsaken world around us. Very narcissistic in nature. 
# Set up the postsqlgre for osm data
1. Install the postsql-gre-9.1
2. Create a database named 'osm'
3. Run the following commands based on your host name, username and the location of the *.sql files
   psql -h 127.0.0.1 -U postgres -d osm -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql 
   psql -h 127.0.0.1 -U postgres -d osm -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
4. Install osm2pgsql.
5. Run the below command to convert data from osm into database.
   osm2pgsql -l -p osm -d osm -U postgres -H 127.0.0.1 -W PATH_TO_OSM_FILE

OR 

# Restore from backup
1. Run the command to restore from the dump (Postgresql) static/osm/osm.backup
   psql dbname < infile ( Please take care to first create the database )

# Set up the places_attribute table
1. Run the file places/filler.py
   

OR 

# Restore from backup
1. Run the command to restore from the dump (Mysql) static/places/idea.sql
   mysql-uroot -proot idea < ideal.sql

# Install the redis
# Install the redis-py from the below mentioned link
  https://github.com/andymccurdy/redis-py/

Commands to take backup of postgresql
pg_dump -h 127.0.0.1 -U postgres -W osm > osm.backup


