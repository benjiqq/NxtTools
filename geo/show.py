""" 
show 
"""

import pymongo as pym
import random as ra
import time

p = 3001
con = pym.Connection(host='127.0.0.1', port=p)

db = con.meteor

print 'all collections'
cols = db.collection_names()
print '*'*30
print '>> collections '
print '*'*30
for c in cols:
    print c

for p in db.peers.find()[:5]:
    print p
