import sys
sys.path.append("../api") 

from nxtapi import *
import urllib2
import socket
import json

def get_peers():
    url = build_req("getPeers")
    j = make_req(url)
    return j


def test_port(peer):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    result = sock.connect_ex((peer,80))
    if result == 0:
        print "Port is open ",peer
        return True
    
        #s = urllib.urlopen("http://" + peer).read()
        #if s != "":
        #    with open(peer + '.html','w') as f:
        #        f.write(s)

    else:
        return False
    #    print "Port is not open"

def get_geo(peers):
    g = list()

    for p in peers[:]:
        u = "http://www.telize.com/geoip/" + p
        s = urllib2.urlopen(u).read()
        j = json.loads(s)
        lat = j["latitude"]
        lon = j["longitude"]
        g.append((lat,lon))
        print lat,lon

    return g



peers = get_peers()['peers']
print 'number of peers ',len(peers)

print 'a peer => ',peers[0]
#g = get_geo(peers)
#with open('geo.csv','w') as f:
#    for x in g:
#        f.write(str(
