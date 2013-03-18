from django.contrib import admin
from ideac.models import PlaceType, TypeRelation

class PlaceTypeAdmin(admin.ModelAdmin):
   pass

admin.site.register(PlaceType, PlaceTypeAdmin)


