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

@never_cache
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

@never_cache
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
  
  #print message
  #proc = subprocess.Popen(['gnuplot', '-p'],
	#	shell=True,
	#	stdin=subprocess.PIPE,
	#	)
  #f = open("/home/florian/test.dat", "w")
  #for i in  range(len(message["L1"])-1,len(message["L1"])-10, -1):
#	f.write("%s \n" % (str(message["PubDate"][i]) + "\t" + str(message["L1"][i] * 1000) + "\t" + str(message["L2"][i] * 1000) + "\t" + str(message["L3"][i] * 1000 ))) 
 # f.close()
  #f.write("%s \n" % '\t'.join([str(i) for i in mydict["L2"]]))
  #proc.stdin.write('set terminal svg size 600,400\n')
  #proc.stdin.write('set output \'/home/florian/plotting.svg\' \n')
  #proc.stdin.write('set grid \n')
  #proc.stdin.write('set xlabel "Time" \n')
  #proc.stdin.write('set xdata time \n')
  #proc.stdin.write('set timefmt "%d/%m/%H:%M:%S"\n')
  #proc.stdin.write('set format x "%d/%m\\n%H:%M:%S"\n')
  #proc.stdin.write('set ylabel "Values"\n')
  #proc.stdin.write("""plot "/home/florian/test.dat" using 1:2 with linespoints title "Test", \
	#"/home/florian/test.dat" using 1:3 with linespoints title "L2", \
	#	"/home/florian/test.dat" using 1:4 with linespoints title "L3" \n""")
  #proc.stdin.write("quit\n")
  myjson = json.dumps(message)
  #print myjson
  return HttpResponse(myjson, mimetype='application/json')
  
@never_cache
@csrf_exempt
def internal(request):
  now = datetime.datetime.now()
  onehour = now - datetime.timedelta(hours= 1)
  mylist = Data.objects.filter(pub_date__range=(onehour, now)).order_by('-pub_date')[:1].values()
  print mylist
  message = {"L1" : round(mylist[0]["l1"]*1000, 2), "L2": round(mylist[0]["l2"]*1000,2), "L3": round(mylist[0]["l3"]*1000,2), "Sum": round(mylist[0]["sum"]*1000,2), "PubDate" : mylist[0]["pub_date"].strftime('%d/%m/%H:%M:%S')} 
  print message
  myjson = json.dumps(message)
  return HttpResponse(myjson, mimetype='application/json')