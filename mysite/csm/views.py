# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from csm.models import Data

@csrf_exempt
def index(request):
  t = loader.get_template("index.html")
  mylist = Data.objects.all().order_by('-pub_date')[:5]
  c = Context({
        'mylist': mylist,
    })
  print "index stuff"
  return HttpResponse(t.render(c))
  
@csrf_exempt
def stuff(request):
  mylist = Data.objects.all().order_by('-pub_date')[:5]
  message = {"L1": "", "L2": "", "L3": "", "Sum": "", "PubDate": ""}
  message["L1"] = mylist.l1
  message["L2"] = mylist.l2
  message["L3"] = mylist.l3
  message["Sum"] = mylist.sum
  message["PubDate"] = mylist.pub_date
  json = simplejson.dumps(message)
  print mylist
  print "Look if I'm here"
  return HttpResponse(json, mimetype='application/json')