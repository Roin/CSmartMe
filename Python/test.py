#/usr/bin/env python

import serial, string, time, re, sqlite3, datetime
import CSMSerialHandler

#vars
values = []
r = re.compile("\((\d*\.\d*)\*")
connector = sqlite3.connect('/home/florian/study.db')
c = connector.cursor()

#s = serial.Serial("/dev/ttyUSB0", 9600, serial.SEVENBITS, serial.PARITY_EVEN, serial.STOPBITS_ONE)
#s.write("/?!" + chr(13) + chr(10))
c.execute('PRAGMA journal_mode=WAL;')
c.execute('PRAGMA page_size = 4096;')
c.execute('PRAGMA cache_size=10000;')
c.execute('PRAGMA locking_mode=EXCLUSIVE;')
c.execute('PRAGMA synchronous=NORMAL;')
c.execute('PRAGMA cache_size=5000;')
c.execute('PRAGMA temp_store = MEMORY;')
s = CSMSerialHandler.CSMSerialHandler("/dev/ttyUSB0", 9600)
s.CSMWrite("/?!" + chr(13) + chr(10))
teststring = s.CSMRead()
print teststring
time.sleep(1)
s.CSMWrite(chr(6) + "050" + chr(13) + chr(10))
time.sleep(1)
while 1:
 mystring = s.CSMRead()
 if(r.search(mystring)):
   values.append(float(r.search(mystring).group(1)))
 print mystring
 if ("!" in mystring):
	 c.execute("INSERT INTO csm_data(l1, l2, l3, sum, pub_date) VALUES (?, ?, ?, ?, ? );", (values[4], values[5], values[6], values[7], datetime.datetime.now()))
	 connector.commit()
	 values=[]
	 time.sleep(1)
	 s.CSMWrite("/?!" + chr(13) + chr(10))
         time.sleep(1)
         s.CSMWrite(chr(6) + "050" + chr(13) + chr(10))
 if len(mystring) == 0:
   s.CSMWrite("/?!" + chr(13) + chr(10))
   time.sleep(1)
   s.CSMWrite(chr(6) + "050" + chr(13) + chr(10))
