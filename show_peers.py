from nxtapi import *
import urllib
import socket

peers = get_peers()['peers']
print 'number of peers ',len(peers)

print 'a peer => ',peers[0]

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


c = 0
for p in peers:
    #print p
    if test_port(p):
        c+=1

print 'total open ports 80' ,c

"""
 python show_peers.py 
number of peers  328
a peer  85.214.222.82
"""
