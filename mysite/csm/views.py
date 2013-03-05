# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
#from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from csm.models import Data
import json
import subprocess
import datetime

@csrf_exempt
def index(request):
  t = loader.get_template("index.html")
  now = datetime.datetime.now()
  onehour = now - datetime.timedelta(hours= 1)
  mylist = Data.objects.filter(pub_date__range=(onehour, now))[:10].values()
  c = Context({
        'mylist': mylist,
    })
  print "index stuff"
  return HttpResponse(t.render(c))

@csrf_exempt
def stuff(request):
  print datetime.datetime.now().day
  now = datetime.datetime.now()
  onehour = now - datetime.timedelta(hours= 1)
  print onehour
  mylist = Data.objects.filter(pub_date__range=(onehour, now)).order_by('-pub_date')[:10].values()
  message = {"L1" : [], "L2": [], "L3": [], "Sum": [], "PubDate" : []} 
  for i in mylist:
    message["L1"].append(round(i["l1"]*1000, 2))
    message["L2"].append(round(i["l2"]*1000, 2))
    message["L3"].append(round(i["l3"]*1000, 2))
    message["Sum"].append(round(i["sum"]*1000, 2))
    message["PubDate"].append(i["pub_date"].strftime('%d/%m/%H:%M:%S'))
  myjson = json.dumps(message)
  #print myjson
  return HttpResponse(myjson, mimetype='application/json')
  
@csrf_exempt
def internal(request):
  now = datetime.datetime.now()
  onehour = now - datetime.timedelta(minutes= 10)
  #mylist = Data.objects.filter(pub_date__range=(onehour, now)).order_by('-pub_date')[1].values()
  mylist = Data.objects.filter(pub_date__range=(onehour, now)).order_by('pub_date').latest().values()
  print mylist
  message = {"L1" : round(mylist["l1"]*1000, 2), "L2": round(mylist["l2"]*1000,2), "L3": round(mylist["l3"]*1000,2), "Sum": round(mylist["sum"]*1000,2), "PubDate" : mylist["pub_date"].strftime('%d/%m/%H:%M:%S')} 
  #print message
  myjson = json.dumps(message)
  return HttpResponse(myjson, mimetype='application/json')