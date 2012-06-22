from consts import *
from django.db.models import Q
import math

from ideacalculator.models import Place, TypeRelation

def getWeightage(origin, placeComb):
    points = 0
    favFactor = None
    maxWt = 0
    p1, p2 = getPlaces(placeComb)
    try:
        t1 = PlaceType.objects.get(name=p1.getType())
        t2 = PlaceType.objects.get(name=p2.getType())
    except:
        return 0, None
    time, day = getTime()
    weather = getWeather()

    # PLACE POINTS
    w = PLACE_WT*((t1.place_pt+t2.place_pt)/2)
    points += w
    if(w>maxWt):
        maxWt = w
        favFactor = PLACE_FACTOR_TEXT

    # TIME POINTS
    f1 = 0
    for f_c in t1.get_fav_times():
        if(f_c[0]<=time and f_c[1]>=time):
            f1=10
    f2 = 0
    for f_c in t2.get_fav_times():
        if(f_c[0]<=time and f_c[1]>=time):
            f2=10
    w = TIME_WT*((f1+f2)/2)
    points += w
    if(w>maxWt):
        maxWt = w
        favFactor = TIME_FACTOR_TEXT

    # WEATHER POINTS
    f1 = 0
    if weather in t1.get_fav_weathers():
        f1=10
    f2 = 0
    if weather in t2.get_fav_weathers():
        f2=10
    w = WEATHER_WT*((f1+f2)/2)
    points += w
    if(w>maxWt):
        maxWt = w
        favFactor = WEATHER_FACTOR_TEXT

    # DAY POINTS
    f1 = 0
    if day in t1.get_fav_days():
        f1=10
    f2 = 0
    if day in t2.get_fav_days():
        f2=10
    w = DAY_WT*((f1+f2)/2)
    points += w
    if(w>maxWt):
        maxWt = w
        favFactor = DAY_FACTOR_TEXT

    #LOCATON
    w = int(LOCATON_WT*(((180-getAngle(origin, p1, p2)/180)*5)+((SEARCH_RADIUS-getDist(p2, origin)/SEARCH_RADIUS)*5)))
    points += w
    if(w>maxWt):
        maxWt = w
        favFactor = LOCATON_FACTOR_TEXT

    #COMBINAION
    w = 0
    q = (Q(type1=t1)&Q(type2=t2))|(Q(type1=t2)&Q(type2=t1))
    r = TypeRelation.objects.filter(q)
    if r:
        w = COMBINATION_WT*r[0].points
    points += w
    if(w>maxWt):
        maxWt = w
        favFactor = COMBINATION_FACTOR_TEXT
    return points, favFactor


def getTime():
    time = None
    return time


def getWeather():
    weather = None
    return weather


def getNearbyPlaces(origin, radius = SEARCH_RADIUS):
    '''
    Return places in the radius
    '''
    places = []
    olat = origin.getLat()
    olng = origin.getLng()
    #q = Q(lat__lt=olat-SEARCH_BOX_LENGTH) | Q()
    qry = Place.objects.all()
    for p in qry:
        if(getDist(origin, p)<SEARCH_RADIUS):
            places.append(p)
    return places


def getPlaceCombs(origin, places):
    '''
    Return nC2 place combinations
    '''
    placeCombs = []
    i = 1
    for place1 in places:
        for place2 in places[i:]:
            if(getDist(origin, place1) < getDist(origin, place2)):
                p1=place1
                p2=place2
            else:
                p1=place2
                p2=place1
            placeCombs.append([p1, p2])
        i +=1
    return placeCombs

def getSentence(p1, p2, factor):
    return "Go to "+str(p2.name)+" through "+str(p1.name)+". "+str(factor)+" is favourable"

def getPlaces(placeComb):
    return placeComb[0], placeComb[1]


def getAngle(origin, p1, p2):
    return 0


def getDist(p1, p2):
    lat1 = p1.getLat()
    lng1 = p1.getLng()
    lat2 = p2.getLat()
    lng2 = p2.getLng()
    return distance_on_unit_sphere(lat1, lng1, lat2, lng2)


def distance_on_unit_sphere(lat1, long1, lat2, long2):

    # Convert latitude and longitude to
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0

    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians

    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians

    # Compute spherical distance from spherical coordinates.

    # For two locations in spherical coordinates
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) =
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length

    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth
    # in your favorite set of units to get length.
    return arc*6373