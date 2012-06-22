from ideacalculator.models import Place, PlaceType, TypeRelation
from ideacalculator.utils import getNearbyPlaces, getPlaceCombs, getWeightage, getSentence, getPlaces

from django.utils import simplejson
from operator import itemgetter
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def homepage(request):
    places = Place.objects.all()
    return render_to_response('home.html', {'places': places})

@csrf_exempt
def getideas(request):
    if request.method.upper() == 'POST':
        origin = Place.objects.get(pk=request.POST.get("place_id"))
        nearbyPlaces = getNearbyPlaces(origin)
        placeCombs = getPlaceCombs(origin, nearbyPlaces)
        ideas = []
        for placeComb in placeCombs:
            p1, p2 = getPlaces(placeComb)
            points, factor = getWeightage(origin, placeComb)
            sentence = getSentence(p1, p2, factor)
            ideas.append({
                        'place1': p1.name,
                        'place2': p2.name,
                        'points': points,
                        'sentence': sentence})
        ideas.sort(key=itemgetter('points'))
        return render_to_response('idea.html', {'ideas': ideas})