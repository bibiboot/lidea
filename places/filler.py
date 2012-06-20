import pdb
import urllib2
from django.db import connections, transaction
from places.models import Attribute
from osm.models import Point

def basic_filling():
    for d in Point.objects.exclude(name=''):
        try:
            lat, lon = lat_long(d.osm_id)
            basic_save(d, lat, lon)
        except Exception,e:
            print str(e)

def lat_long(osm_id):
    """
    Calculate the latitude and longitude
    """
    cur = connections['osm'].cursor()
    cur.execute("select osm_id, ST_AsText(way) from osm_point where osm_id='%s'"%osm_id)
    row = cur.fetchone()
    geo = row[1]
    geo = geo.replace('POINT','')
    geo = geo.replace('(','')
    geo = geo.replace(')','')
    llist = geo.split(' ')
    lat, lon = llist[1],llist[0]
    return lat, lon

def basic_save(d,lat,lon):
    obj, created = Attribute.objects.get_or_create(osm_id=d.osm_id,
                                           lat=lat,
                                           lon=lon,
                                           name=d.name,
                                           aerialway=d.aerialway, 
                                           aeroway=d.aeroway,
                                           amenity=d.amenity,
                                           area=d.area,
                                           barrier=d.barrier,
                                           bicycle=d.bicycle,
                                           bridge=d.bridge,
                                           boundary=d.boundary,
                                           building=d.building,
                                           capital=d.capital,
                                           construction=d.construction,
                                           cutting=d.cutting,
                                           disused=d.disused,
                                           ele=d.ele,
                                           embankment=d.embankment,
                                           foot=d.foot,
                                           highway=d.highway,
                                           historic=d.historic,
                                           horse=d.horse,
                                           junction=d.junction,
                                           landuse=d.landuse,
                                           layer=d.layer,
                                           leisure=d.leisure,
                                           lock=d.lock,
                                           man_made=d.man_made,
                                           military=d.military)

def detail_inf(lat, lon):
    url = "http://nominatim.openstreetmap.org/reverse?format=json&lat=%s&lon=%s" % (lat,lon)
    data = urllib2.urlopen(url).read()
    return eval(data)

def detail_filling():
    for attr in Attribute.objects.filter(display_name=None):
        try:
            data = detail_inf(attr.lat, attr.lon)
            detail_save(attr, data)
        except Exception,e:
            print str(e), attr.osm_id

def detail_save(attr, data):
    attr.display_name = data['display_name']
    attr.address = data['address']
    attr.county = data['address'].get('county','')
    attr.suburb = data['address'].get('suburb','')
    attr.state_district = data['address'].get('state_district','')
    attr.postcode = data['address'].get('postcode','')
    attr.country_code = data['address'].get('county_code','')
    attr.country = data['address'].get('country','')
    attr.state = data['address'].get('state','')
    attr.city = data['address'].get('city','')
    attr.road = data['address'].get('road','')
    attr.village = data['address'].get('village','')

    attr.save()
                        
basic_filling()
detail_filling()
