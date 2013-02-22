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
  mylist = Data.objects.all().order_by('-pub_date')[:5].values()
  message = {"L1": "", "L2": "", "L3": "", "Sum": "", "PubDate": ""}
  for i in mylist:
    message["L1"].append(i["l1"])
    message["L2"].append(i["l2"])
    message["L3"].append(i["l3"])
    message["Sum"].append(i["sum"])
    message["PubDate"].append(i["pub_date"])
  print message
  message = {"y0" : "Yo"}
  json = simplejson.dumps(message)
  #print mylist.l1
  print "Look if I'm here"
  return HttpResponse(json, mimetype='application/json')