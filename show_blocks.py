"""
show baseTarget for a number of blocks
"""

from nxtapi import *

sh = 1

print '*'*20
print '>> baseTarget %i'%sh 
print '*'*20

for h in range(sh,sh+30):
    blocks = req("getBlock",height=str(h))
    print '%i  %s'%(h, blocks['baseTarget'])

