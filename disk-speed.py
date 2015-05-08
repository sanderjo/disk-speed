#!/usr/bin/env python

import time, os, sys

def writetofile(filename,mysize):
	mystring = "The quick brown fox jumps over the lazy dog"
	writeloops = int(mysize/len(mystring))

	try:
		f = open(filename, 'w')
	except:
		print "Error writing"
		raise
	for x in range(0, writeloops):
		f.write(mystring)
	f.close()
	os.remove(filename)

############## Start of main


filename = 'outputTESTING.txt'	# default filename
filesize = 1000000
maxtime = 0.5 # in sec

if len(sys.argv) >= 2:
	arg1 = sys.argv[1]
	if os.path.isdir(arg1): 
		filename = os.path.join(arg1,filename)
	elif os.path.isfile(arg1):
		filename = arg1
	else:
		print "Not a filename nor a directory. Bailing out"
		sys.exit(1)
#print "filename is", filename
print "Absolute path of filename ", os.path.abspath(filename)


start = time.time()
loopcounter = 0
while True:
	try:
		writetofile(filename, filesize)
	except:
		print "EERRRROOROROR ... bailing out"
		sys.exit(0)
	loopcounter += 1
	now = time.time()
	diff = now-start
	if diff > maxtime: break

#print "diff is", diff, "msec"
#print loopcounter*filesize/1000000, "Mbytes written"
print "Disk writing speed:", (loopcounter*filesize/1000000)/diff, "Mbytes per second"

