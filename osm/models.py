from django.db import models
from django.contrib import admin

class Point(models.Model):
    osm_id =models.IntegerField(primary_key=True)
    z_order =models.IntegerField()
    way = models.CharField(max_length=100)
    access = models.CharField(max_length=100)
    #addr:housenumber = models.CharField(max_length=100)
    #addr:interpolation = models.CharField(max_length=100)
    admin_level = models.CharField(max_length=100)
    aerialway = models.CharField(max_length=100)
    aeroway = models.CharField(max_length=100)
    amenity = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    barrier = models.CharField(max_length=100)
    bicycle = models.CharField(max_length=100)
    bridge = models.CharField(max_length=100)
    boundary = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    construction = models.CharField(max_length=100)
    cutting = models.CharField(max_length=100)
    disused = models.CharField(max_length=100)
    ele = models.CharField(max_length=100)
    embankment = models.CharField(max_length=100)
    foot = models.CharField(max_length=100)
    highway = models.CharField(max_length=100)
    historic = models.CharField(max_length=100)
    horse = models.CharField(max_length=100)
    junction = models.CharField(max_length=100)
    landuse = models.CharField(max_length=100)
    layer = models.CharField(max_length=100)
    leisure = models.CharField(max_length=100)
    lock = models.CharField(max_length=100)
    man_made = models.CharField(max_length=100)
    military = models.CharField(max_length=100)
    motorcar = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    natural = models.CharField(max_length=100)
    oneway = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)
    poi = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    power_source = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    railway = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    tourism = models.CharField(max_length=100)
    tunnel = models.CharField(max_length=100)
    waterway = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    wood = models.CharField(max_length=100)               

class Line(models.Model):
    osm_id =models.IntegerField(primary_key=True)
    access = models.CharField(max_length=100)
    #addr:housenumber = models.CharField(max_length=100)
    #addr:interpolation = models.CharField(max_length=100)
    admin_level = models.CharField(max_length=100)
    aerialway = models.CharField(max_length=100)
    aeroway = models.CharField(max_length=100)
    amenity = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    barrier = models.CharField(max_length=100)
    bicycle = models.CharField(max_length=100)
    bridge = models.CharField(max_length=100)
    boundary = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    construction = models.CharField(max_length=100)
    cutting = models.CharField(max_length=100)
    disused = models.CharField(max_length=100)
    embankment = models.CharField(max_length=100)
    foot = models.CharField(max_length=100)
    highway = models.CharField(max_length=100)
    historic = models.CharField(max_length=100)
    horse = models.CharField(max_length=100)
    junction = models.CharField(max_length=100)
    landuse = models.CharField(max_length=100)
    layer = models.CharField(max_length=100)
    leisure = models.CharField(max_length=100)
    lock = models.CharField(max_length=100)
    man_made = models.CharField(max_length=100)
    military = models.CharField(max_length=100)
    motorcar = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    natural = models.CharField(max_length=100)
    oneway = models.CharField(max_length=100)
    operator = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    power_source = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    railway = models.CharField(max_length=100)
    ref = models.CharField(max_length=100)
    religion = models.CharField(max_length=100)
    route = models.CharField(max_length=100)
    service = models.CharField(max_length=100)
    shop = models.CharField(max_length=100)
    sport = models.CharField(max_length=100)
    tourism = models.CharField(max_length=100)
    tracktype = models.CharField(max_length=100)
    tunnel = models.CharField(max_length=100)
    waterway = models.CharField(max_length=100)
    width = models.CharField(max_length=100)
    wood = models.CharField(max_length=100)
    z_order = models.IntegerField(max_length=100)
    way_area = models.IntegerField(max_length=100)
    way = models.CharField(max_length=100)

class Roads(models.Model):
    osm_id = models.IntegerField(primary_key=True)
    access  = models.CharField(max_length=100)
    #addr:housenumber  = models.CharField(max_length=100)
    #addr:interpolation  = models.CharField(max_length=100)
    admin_level  = models.CharField(max_length=100)
    aerialway  = models.CharField(max_length=100)
    aeroway  = models.CharField(max_length=100)
    amenity  = models.CharField(max_length=100)
    area  = models.CharField(max_length=100)
    barrier  = models.CharField(max_length=100)
    bicycle  = models.CharField(max_length=100)
    bridge  = models.CharField(max_length=100)
    boundary  = models.CharField(max_length=100)
    building  = models.CharField(max_length=100)
    construction  = models.CharField(max_length=100)
    cutting  = models.CharField(max_length=100)
    disused  = models.CharField(max_length=100)
    embankment  = models.CharField(max_length=100)
    foot  = models.CharField(max_length=100)
    highway  = models.CharField(max_length=100)
    historic  = models.CharField(max_length=100)
    horse  = models.CharField(max_length=100)
    junction  = models.CharField(max_length=100)
    landuse  = models.CharField(max_length=100)
    layer  = models.CharField(max_length=100)
    leisure  = models.CharField(max_length=100)
    lock  = models.CharField(max_length=100)
    man_made  = models.CharField(max_length=100)
    military  = models.CharField(max_length=100)
    motorcar  = models.CharField(max_length=100)
    name  = models.CharField(max_length=100)
    natural  = models.CharField(max_length=100)
    oneway  = models.CharField(max_length=100)
    operator  = models.CharField(max_length=100)
    power  = models.CharField(max_length=100)
    power_source  = models.CharField(max_length=100)
    place  = models.CharField(max_length=100)
    railway  = models.CharField(max_length=100)
    ref  = models.CharField(max_length=100)
    religion  = models.CharField(max_length=100)
    route  = models.CharField(max_length=100)
    service  = models.CharField(max_length=100)
    shop  = models.CharField(max_length=100)
    sport  = models.CharField(max_length=100)
    tourism  = models.CharField(max_length=100)
    tracktype  = models.CharField(max_length=100)
    tunnel  = models.CharField(max_length=100)
    waterway  = models.CharField(max_length=100)
    width  = models.CharField(max_length=100)
    wood  = models.CharField(max_length=100)
    z_order = models.IntegerField()
    way_area = models.IntegerField()
    way = models.CharField(max_length=100)

class PointAdmin(admin.ModelAdmin):
    list_display=('osm_id','name','amenity','z_order',
'access',
'admin_level',
'aerialway',
'aeroway',
'amenity',
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

class LineAdmin(admin.ModelAdmin):
    list_display=('osm_id','name','amenity',
'access',
'admin_level',
'aerialway',
'aeroway',
'area',
'barrier',
'bicycle',
'bridge',
'boundary',
'building',
'construction',
'cutting',
'disused',
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
'tracktype',
'tunnel',
'waterway',
'width',
'wood',
'z_order',
'way_area',
'way')

class RoadsAdmin(admin.ModelAdmin):
    list_display=('osm_id','name','highway','bridge',
'amenity',
'access',
'admin_level',
'aerialway',
'aeroway',
'area',
'barrier',
'bicycle',
'boundary',
'building',
'construction',
'cutting',
'disused',
'embankment',
'foot',
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
'tracktype',
'tunnel',
'waterway',
'width',
'wood',
'z_order',
'way_area',
'way')

"""
admin.site.register(Point, PointAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(Roads, RoadsAdmin)
"""
