from django.contrib import admin
from ideacalculator.models import PlaceType, TypeRelation

class PlaceTypeAdmin(admin.ModelAdmin):
   pass

admin.site.register(PlaceType, PlaceTypeAdmin)


