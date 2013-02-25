# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
#from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from csm.models import Data
import json
import subprocess

@csrf_exempt
def index(request):
  t = loader.get_template("index.html")
  mylist = Data.objects.all().order_by('-pub_date')[:10]
  c = Context({
        'mylist': mylist,
    })
  print "index stuff"
  return HttpResponse(t.render(c))
  
@csrf_exempt
def stuff(request):
  mylist = Data.objects.all().filter(pub_date__day=datetime.datetime.now().day)[:10].values()
  message = {"L1" : [], "L2": [], "L3": [], "Sum": [], "PubDate" : []} 
  for i in mylist:
    message["L1"].append(i["l1"])
    message["L2"].append(i["l2"])
    message["L3"].append(i["l3"])
    message["Sum"].append(i["sum"])
    message["PubDate"].append(i["pub_date"].strftime('%d/%m/%H:%M:%S'))
  #print message
  proc = subprocess.Popen(['gnuplot', '-p'],
		shell=True,
		stdin=subprocess.PIPE,
		)

  f = open("/home/florian/test.dat", "w")
  for i in  range(0,len(message["L1"])-1):
	f.write("%s \n" % (str(message["PubDate"][i]) + "\t" + str(message["L1"][i] * 1000) + "\t" + str(message["L2"][i] * 1000) + "\t" + str(message["L3"][i] * 1000 ))) 
  f.close()
  #f.write("%s \n" % '\t'.join([str(i) for i in mydict["L2"]]))
  proc.stdin.write('set terminal svg \n')
  proc.stdin.write('set output \'/home/florian/plotting.svg\' \n')
  proc.stdin.write('set grid \n')
  proc.stdin.write('set xlabel "Time" \n')
  proc.stdin.write('set xdata time \n')
  proc.stdin.write('set timefmt "%d/%m/%H:%M:%S"\n')
  proc.stdin.write('set format x "%d/%m\\n%H:%M:%S"\n')
  proc.stdin.write('set ylabel "Values"\n')
  proc.stdin.write("""plot "/home/florian/test.dat" using 1:2 with linespoints title "Test", \
		"/home/florian/test.dat" using 1:3 with linespoints title "L2", \
		"/home/florian/test.dat" using 1:4 with linespoints title "L3" \n""")
  proc.stdin.write("quit\n")
  print "Check if finished"
  datadict = {"Path" : "/home/florian/plotting.svg"}
  myjson = json.dumps(datadict)
  print myjson
  print "Look if I'm here"
  return HttpResponse(myjson, mimetype='application/json')