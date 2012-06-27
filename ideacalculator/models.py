from django.db import models
from consts import NAME_MAX_LENGTH
from django.contrib import admin

class Place(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    amenity = models.CharField(max_length=NAME_MAX_LENGTH)
    lat = models.FloatField()
    lng = models.FloatField()

    def getType(self):
        return self.amenity

    def getLat(self):
        return self.lat/10000000

    def getLng(self):
        return self.lng/10000000

class PlaceType(models.Model):
   name = models.CharField(max_length=NAME_MAX_LENGTH)
   place_pt = models.PositiveIntegerField()
   fav_time = models.TextField(blank=True,
                               null=True)
   fav_weather = models.TextField(blank=True,
                               null=True)
   fav_day = models.TextField(blank=True,
                               null=True)

   def get_fav_times(self):
       return []

   def get_fav_weathers(self):
       return []

   def get_fav_days(self):
       return []

class PlaceTypeAdmin(admin.ModelAdmin):
   pass

class TypeRelation(models.Model):
   type1 = models.ForeignKey(PlaceType, related_name='type1')
   type2 = models.ForeignKey(PlaceType, related_name='type2')
   points = models.PositiveIntegerField()
   fav_time = models.TextField(blank=True,
                               null=True)
   fav_weather = models.TextField(blank=True,
                               null=True)
   fav_day = models.TextField(blank=True,
                               null=True)

#admin.site.register(PlaceType, PlaceTypeAdmin)
