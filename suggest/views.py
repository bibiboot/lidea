import pdb
import simplejson
from django.http import HttpResponse
from django.core.cache import get_cache
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    """
    Landing method
    """
    if True:
        return render_to_response('home/home.html',{}, RequestContext(request, { }) )
    else:
        return render_to_response('home/home.html',{}, RequestContext(request, { }) )

def autosuggest(request):
    """
    Auto suggest landing method
    """
    try:
        if (request.GET.has_key('search')):
            searchWord = request.GET['search'].lower()
            airList = []
            #airList = search(searchWord)
            airList = searchincludespace(searchWord)
            return HttpResponse(simplejson.dumps(airList))
        else:
            return HttpResponse('{"result":"failed","desc":"No Matches Found"}')
    except Exception,e:
        print e
        return HttpResponse('{"result":"failed","desc":"No Matches Found"}')

def search(word):
    """
    Search for single word
    """
    r = get_cache('autosuggest')
    hashes_list  = r._client.zrange(name="task:%s"%word,start=0, end=-1)
    return answer(hashes_list)

def searchincludespace(words):
    """
    Search in case of multiple words
    """
    r = get_cache('autosuggest')
    set_list = ["task:%s"%word for word in words.split(' ')]
    res = r._client.zinterstore("res", set_list)
    hashes_list = r._client.zrange(name="res", start=0, end=-1)
    return answer(hashes_list)

def answer(hashes_list):
    """
    All the sentences corresponding
    to the hashes dreived
    """
    suggList = []
    r = get_cache('autosuggest')
    for hashes in hashes_list:
        di = {}
        result = r._client.hget("task", hashes)
        rlist = result.split(':')
        di['cityname'] = rlist[0].title()
        di['iatacode'] = rlist[1].title()
        di['osmid'] = hashes
        di['airportname'] = "%s, %s" % (rlist[2].title(), rlist[3].title())
        suggList.append(di)
    return suggList
