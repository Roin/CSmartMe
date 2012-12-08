#/usr/bin/env python

import serial, string, time

s = serial.Serial("/dev/ttyUSB0",9600, serial.SEVENBITS, serial.PARITY_EVEN, serial.STOPBITS_ONE)
s.write("/?!" + chr(13) + chr(10))
teststring = s.readline()
print teststring
time.sleep(1)
s.write(chr(6) + "050" + chr(13) + chr(10))
time.sleep(1)
print "Hier"
while 1:
 mystring = s.readline()
 print mystring
 if ("!" in mystring):
	 time.sleep(1)
	 s.write("/?!" + chr(13) + chr(10))
	 time.sleep(1)
	 s.write(chr(6) + "050" + chr(13) + chr(10))
	 time.sleep(1)

