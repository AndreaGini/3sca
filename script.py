#!/usr/bin/python
import urllib2, base64, json, sys

username="3scale"
password="3scale"

ip = ''
if sys.argv[1:]:
   ip = str(sys.argv[1])
else:
	print "Please provide an ip of your docker container "
	print "Usage: script.py ip port "
	exit()
port = ''
if sys.argv[2:]:
    port = str(sys.argv[2])
else:
	print "Please provide an port of your docker container "
	print "Usage: script.py ip port "
	exit()

dc = urllib2.Request("http://%s:%s/datacenters/" % (ip,port))
sr = urllib2.Request("http://%s:%s/servers/" % (ip,port))


base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
dc.add_header("Authorization", "Basic %s" % base64string)
sr.add_header("Authorization", "Basic %s" % base64string)   
dcurl = urllib2.urlopen(dc)
srurl = urllib2.urlopen(sr)

dcdata = json.load(dcurl)   
srdata = json.load(srurl)


for i,j in enumerate(dcdata):
    print "Datacenter Name:" + j['name']
    for l,k in enumerate(srdata):
        for n in j['servers'].split(","):
        	if str(k['id']) == str(n) : 
        	    print "----------->" + "Server Name: " + k['name'] + "Server Descriprion: " + k['description']

