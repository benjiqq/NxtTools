"""
tiny Nxt API 

http://wiki.nxtcrypto.org/wiki/Nxt_API
"""

import urllib2
import requests
import json

bURL = "http://127.0.0.1:7876/nxt?"


def req(requestType, **kwargs):
    """make a request"""
    url = build_req(requestType, **kwargs)
    return make_req(url)

def build_req(requestType, **kwargs):
    """build a URL for a request"""
    url = bURL +"requestType="+requestType
    for k,v in kwargs.items():
        url +="&"+k+"="+v
    return url

def make_req(url):
    """make the HTTP request"""
    r = requests.get(url)
    j = json.loads(r.content)
    return j



#-----
#examples

def get_Account(accountID):
    url = build_req("getAccount",account=accountID)
    print url
    j = make_req(url)
    return j

def get_tx(accountID):
    url = build_req("getAccountTransactions",account=accountID)
    j = make_req(url)
    return j
    


def get_peers():
    url = build_req("getPeers")
    j = make_req(url)
    return j






