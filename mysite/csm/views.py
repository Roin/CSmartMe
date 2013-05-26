# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
#from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from csm.models import Data
import json
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
  mylist = Data.objects.filter(pub_date__range=(onehour, now)).order_by('-pub_date')[:20].values()
  message = {"L1" : [], "L2": [], "L3": [], "Sum": [], "PubDate" : []} 
  #old format: %d/%m/%H:%M:%S
  for i in mylist:
    message["L1"].append(round(i["l1"]*1000, 2))
    message["L2"].append(round(i["l2"]*1000, 2))
    message["L3"].append(round(i["l3"]*1000, 2))
    message["Sum"].append(round(i["sum"]*1000, 2))
    message["PubDate"].append(i["pub_date"].strftime('%H:%M:%S'))
  myjson = json.dumps(message)
  #print myjson
  return HttpResponse(myjson, mimetype='application/json')
  
@csrf_exempt
def internal(request):
  #now = datetime.datetime.now()
  #onehour = now - datetime.timedelta(minutes= 10)
  #mylist = Data.objects.filter(pub_date__range=(onehour, now)).order_by('-pub_date')[1].values()
  mylist = Data.objects.latest('id')
  print mylist
  #old format: %d/%m/%H:%M:%S
  message = {"L1" : round(mylist.l1*1000, 2), "L2": round(mylist.l2*1000,2), "L3": round(mylist.l3*1000,2), "PubDate" : mylist.pub_date.strftime('%H:%M:%S')} 
  print message
  myjson = json.dumps(message)
  return HttpResponse(myjson, mimetype='application/json')
  
@csrf_exempt
def export(request):
  t = loader.get_template("export.html")
  c = Context({
        'mylist': "Test",
    })
  print "export stuff"
  return HttpResponse(t.render(c))
  
 
@csrf_exempt 
def plot(request):
  from time import strptime
  if request.method == 'POST':
    print request.POST
    if request.POST["aggregate"] == "on":
      print "aggregate is on"
      s1 = request.POST["datepicker1"] + 'T' + request.POST["timepicker1"]
      st = datetime.datetime.strptime(s1, "%d.%m.%YT%H:%M")
      print st
      s2 = request.POST["datepicker2"] + 'T' + request.POST["timepicker2"]
      st2 =  datetime.datetime.strptime(s2, "%d.%m.%YT%H:%M")
      print st2
      mylist = Data.objects.filter(pub_date__range=(st,st2)).order_by('-pub_date').values();
      print "Y0y0y0y0"
      message = {"L1" : [], "L2": [], "L3": [], "Sum": [], "PubDate" : []} 
      for i in mylist:
	message["L1"].append(round(i["l1"]*1000, 2))
	message["L2"].append(round(i["l2"]*1000, 2))
	message["L3"].append(round(i["l3"]*1000, 2))
	message["Sum"].append(round(i["sum"]*1000, 2))
	message["PubDate"].append(i["pub_date"].strftime('%H:%M:%S'))
  myjson = json.dumps(message)
  print "done"
  return HttpResponse(myjson, mimetype="application/json")