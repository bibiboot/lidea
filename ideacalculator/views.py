import pdb
from operator import itemgetter
from django.utils import simplejson
from django.shortcuts import render_to_response
from lidea.places.models import Attribute as Place
from django.views.decorators.csrf import csrf_exempt
from ideacalculator.models import PlaceType, TypeRelation
from ideacalculator.utils import getNearbyPlaces, getPlaceCombs, getWeightage, getPlaces

@csrf_exempt
def getideas(request):
    """
    Calculate the idea + verb and emit
    """
    if request.method.upper() == 'GET':
        try:
            osm_id = request.GET['osmid']
        except Exception, e:
            raise e
        origin = Place.objects.get(osm_id=osm_id)
        nearbyPlaces = getNearbyPlaces(origin)
        placeCombs = getPlaceCombs(origin, nearbyPlaces)
        ideas = []
        for placeComb in placeCombs:
            p1, p2 = getPlaces(placeComb)
            points, factor = getWeightage(origin, placeComb)
            factors = [ factor, 'factor1', 'factor2' ]
            verb1, verb2 = 'verb1','verb2'
            if (points >0):
                ideas.append({
                        'place1' : p1.name,
                        'place2' : p2.name,
                        'verb1'  : verb1,
                        'verb2'  : verb2,
                        'factors': factors,
                        'points' : points,
                        })
        # Sort according to the points
        ideas.sort(key=itemgetter('points'), reverse=True)
        return render_to_response('ideacalculator/idea.html', {'ideas': ideas})
