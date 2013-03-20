import pdb
from operator import itemgetter
from django.utils import simplejson
from django.shortcuts import render_to_response
from lidea.places.models import Attribute as Place
from django.views.decorators.csrf import csrf_exempt
from ideac.utils import getNearbyTheatres
from django.http import HttpResponse


from event.event_filler import view_events_by_lat_lon

@csrf_exempt
def getideas(request):
    """
    Calculate the idea + verb and emit
    """
    ideas = []
    if request.method.upper() == 'GET':
        try:
            osm_id = request.GET['osmid']
        except Exception, e:
            raise e
        lat_s, lat_e, lon_s, lon_e = bounding_box(osm_id)
        """
        origin = Place.objects.get(osm_id=osm_id)
        nearbyThe = getNearbyTheatres(origin)
        for the in nearbyThe:
            ideas.append({
                        'name'   : the.name,
                        'suburb' : the.suburb,
                        'city'   : the.city,
                        'state'  : the.state,
                        'factors': [],
                        'points' : 100,
                       })
        print ideas
        """
        theaters = view_events_by_lat_lon()
        theaters = dummy_data()
        #{'lat': 970, 'occu': 53, 'total': 11, 'lon': 758, 'corner': 8, 'name': '11'}
        #return render_to_response('ideac/idea.html', {'theaters': theaters})
        return HttpResponse(str(theaters))

def dummy_data():
    return [{'name': 'Theater-1', 'occu': 6, 'lon': 96, 'lat': 932, 'corner': 7, 'total': 34}, 
            {'name': 'Theater-2', 'occu': 33, 'lon': 87, 'lat': 943, 'corner': 0, 'total': 29}, 
            {'name': 'Theater-3', 'occu': 9, 'lon': 50, 'lat': 960, 'corner': 0, 'total': 30}, 
            {'name': 'Theater-4', 'occu': 82, 'lon': 635, 'lat': 976, 'corner': 2, 'total': 43}]



def bounding_box(osm_id):
    return 0, 0, 0, 0
