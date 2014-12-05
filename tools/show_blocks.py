"""
show baseTarget for a number of blocks

"""

import sys
sys.path.append("../api") 

from nxtapi import *

sh = 1

print '*'*20
print 'block >> baseTarget delta  (starting %i)'%sh 
print '*'*20

bts = list()

numb = 20
oldt = -1
for h in range(sh,sh+numb):
    blocks = req("getBlock",height=str(h))
    #print blocks
    t = int(blocks['timestamp'])
    delta = t - oldt
    oldt = t
    bt = int(blocks['baseTarget'])
    print '%i  %i   %i'%(h, bt, delta)
    bts.append(bt)

print sum(bts)
