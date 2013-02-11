# Create your views here.
from django.http import HttpResponse
from django.templates import Context, Loader
from csm.models import Data

def index(request):
  l1_list = 
  return HttpResponse("Hello you are viewing the Index page urrrra!")
