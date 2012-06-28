from ideacalculator.models import PlaceType, TypeRelation
from lidea.places.models import Attribute as Place
from ideacalculator.utils import getNearbyPlaces, getPlaceCombs, getWeightage, getSentence, getPlaces
from django.utils import simplejson
from operator import itemgetter
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getideas(request):
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
            sentence = getSentence(p1, p2, factor)
            if (points >0):
                ideas.append({
                        'place1': p1.name,
                        'place2': p2.name,
                        'points': points,
                        'sentence': sentence})
        ideas.sort(key=itemgetter('points'))
        ideas.reverse()
        return render_to_response('ideacalculator/idea.html', {'ideas': ideas})
