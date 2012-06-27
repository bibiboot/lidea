from django.db import models
from django.contrib import admin

class Attribute(models.Model):
    osm_id =models.IntegerField(primary_key=True)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    name = models.CharField(max_length=300)
    display_name = models.CharField(max_length=300,null=True)
    address = models.CharField(max_length=1000,null=True)

    county = models.CharField(max_length=50,null=True)
    suburb = models.CharField(max_length=50,null=True)
    state_district = models.CharField(max_length=50,null=True)
    postcode = models.CharField(max_length=20,null=True)
    country_code = models.CharField(max_length=20,null=True)
    city = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    road = models.CharField(max_length=50,null=True)
    village = models.CharField(max_length=50,null=True)

    #admin_level = models.CharField(max_length=100, null=True)
    aerialway = models.CharField(max_length=100, null=True)
    aeroway = models.CharField(max_length=100, null=True)
    amenity = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    barrier = models.CharField(max_length=100, null=True)
    bicycle = models.CharField(max_length=100, null=True)
    bridge = models.CharField(max_length=100, null=True)
    boundary = models.CharField(max_length=100, null=True)
    building = models.CharField(max_length=100, null=True)
    capital = models.CharField(max_length=100, null=True)
    construction = models.CharField(max_length=100, null=True)
    cutting = models.CharField(max_length=100, null=True)
    disused = models.CharField(max_length=100, null=True)
    ele = models.CharField(max_length=100, null=True)
    embankment = models.CharField(max_length=100, null=True)
    foot = models.CharField(max_length=100, null=True)
    highway = models.CharField(max_length=100, null=True)
    historic = models.CharField(max_length=100, null=True)
    horse = models.CharField(max_length=100, null=True)
    junction = models.CharField(max_length=100, null=True)
    landuse = models.CharField(max_length=100, null=True)
    layer = models.CharField(max_length=100, null=True)
    leisure = models.CharField(max_length=100, null=True)
    lock = models.CharField(max_length=100, null=True)
    man_made = models.CharField(max_length=100, null=True)
    military = models.CharField(max_length=100, null=True)
    motorcar = models.CharField(max_length=100, null=True)
    name = models.CharField(max_length=100, null=True)
    natural = models.CharField(max_length=100, null=True)
    oneway = models.CharField(max_length=100, null=True)
    operator = models.CharField(max_length=100, null=True)
    poi = models.CharField(max_length=100, null=True)
    power = models.CharField(max_length=100, null=True)
    power_source = models.CharField(max_length=100, null=True)
    place = models.CharField(max_length=100, null=True)
    railway = models.CharField(max_length=100, null=True)
    ref = models.CharField(max_length=100, null=True)
    religion = models.CharField(max_length=100, null=True)
    route = models.CharField(max_length=100, null=True)
    service = models.CharField(max_length=100, null=True)
    shop = models.CharField(max_length=100, null=True)
    sport = models.CharField(max_length=100, null=True)
    tourism = models.CharField(max_length=100, null=True)
    tunnel = models.CharField(max_length=100, null=True)
    waterway = models.CharField(max_length=100, null=True)
    width = models.CharField(max_length=100, null=True)
    wood = models.CharField(max_length=100, null=True)

    def getLat(self):
        return float(self.lat)

    def getLng(self):
        return float(self.lon)

    def getType(self):
        return self.amenity

class AttributeAdmin(admin.ModelAdmin):
    list_display=('osm_id',
                  'name',
                  'lat','lon',
                  'display_name',
                  'address',
                  'county',
                  'suburb',
                  'state_district',
                  'postcode',
                  'country_code',
                  'country',
                  'city',
                  'state',
                  'road',
                  'village',
            
#'admin_level',
'amenity',
'aerialway',
'aeroway',
'area',
'barrier',
'bicycle',
'bridge',
'boundary',
'building',
'capital',
'construction',
'cutting',
'disused',
'ele',
'embankment',
'foot',
'highway',
'historic',
'horse',
'junction',
'landuse',
'layer',
'leisure',
'lock',
'man_made',
'military',
'motorcar',
'natural',
'oneway',
'operator',
'poi',
'power',
'power_source',
'place',
'railway',
'ref',
'religion',
'route',
'service',
'shop',
'sport',
'tourism',
'tunnel',
'waterway',
'width',
'wood')

#admin.site.register(Attribute, AttributeAdmin)
