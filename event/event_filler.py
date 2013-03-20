import pdb
from django.core.cache import get_cache

def view_events_by_lat_lon():
    """
    Provide places between two lats and longs
    """
    result = []
    r = get_cache('event')
    for key in r._client.zrangebyscore('lat', 0, 5000):
        d = r.get(key)
        if d:
            d['name'] = key
            result.append(d)
    return result

class Event_Filler:

    def __init__(self):
        self.r = get_cache('event')

    def events_by_lat_lon(self):
        """
        Add places in the redis sorted set by lat and lon
        """
        for i in range(1000):
            d = self.r.get(str(i))
            if d:
                print d
                self.r._client.zadd('lat', str(i), d['lat'])
                self.r._client.zadd('lon', str(i), d['lon'])

    def dummy_find_places_bounding_box(self):
        pass

ef = Event_Filler()
ef.events_by_lat_lon()
print view_events_by_lat_lon()
