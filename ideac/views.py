import pdb
from operator import itemgetter
from django.utils import simplejson
from django.shortcuts import render_to_response
from lidea.places.models import Attribute as Place
from django.views.decorators.csrf import csrf_exempt
from ideac.utils import getNearbyTheatres

from event.event_filler import view_events_by_lat_lon

@csrf_exempt
def getideas(request):
    """
    Calculate the idea + verb and emit
    """
    pdb.set_trace()
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
        view_events_by_lat_lon()
        view_events_by_lat_lon()
        return render_to_response('ideacalculator/idea.html', {'ideas': ideas})

def bounding_box(osm_id):
    return 0, 0, 0, 0
