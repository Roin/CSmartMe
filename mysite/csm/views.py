# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from csm.models import Data

@csrf_exempt
def index(request):
  t = loader.get_template("index.html")
  
  c = Context({
        'mylist': mylist,
    })
  print "index stuff"
  return HttpResponse(t.render(c))
  
@csrf_exempt
def stuff(request):
  mylist = Data.objects.all().order_by('-pub_date')[:5]
  message = {"Eins" : "Y0"}
  json = simplejson.dumps(mylist)
  print "Look if I'm here"
  return HttpResponse(json)