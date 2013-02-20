# Create your views here.
from django.http import HttpResponse
from django.templates import Context, Loader
from django.utils import simplejson
from csm.models import Data

def index(request):
  t = loader.get_template(csm/index.html)
  return HttpResponse(t)
  
def stuff(request):
  message = {"Eins" : "Y0"}
  json = simplejson.dumps(message)
  return HttpResponse(json, mimetype='application/json')
