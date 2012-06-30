from django.db import models
from consts import NAME_MAX_LENGTH

class PlaceType(models.Model):
   name = models.CharField(choices=(('Cinema','Cinema'),
                                    ('Restaurant','Restaurant'),
                                    ('Parking','Parking'),
                                    ('Garden','Garden'),
                                    ('Mall','Mall'),
                                    ('Highway','Highway'),
                                    ('Historical','Historical'),
                                    ('Cafe','Cafe'),
                                    ('Bakery', 'Bakery'),
                                    ('Sweets', 'Sweets'),
                                    ('Lake','Lake'),
                                    ('Beach', 'Beach'),
                                    ('Icecream-parlor', 'Icecream-parlor')), max_length=50)

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
