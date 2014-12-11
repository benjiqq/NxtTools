from nxtapi import *

def get_peers():
    url = build_req("getPeers")
    j = make_req(url)
    return j

peers = get_peers()['peers']
print 'number of peers ',len(peers)
