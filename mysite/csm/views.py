# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.utils import simplejson
from csm.models import Data

def index(request):
  t = loader.get_template("index.html")
  mylist = Data.objects.all().order_by('-pub_date')[:5]
  c = Context({
        'mylist': mylist,
    })
  return HttpResponse(t.render(c))
  
def stuff(request):
  message = {"Eins" : "Y0"}
  json = simplejson.dumps(message)
  return HttpResponse(json, mimetype='application/json')
