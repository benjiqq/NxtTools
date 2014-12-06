"""
show baseTarget for a number of blocks

"""

import sys
sys.path.append("../api") 

from nxtapi import *


print req("getAccountAssets",account="NXT-4VNQ-RWZC-4WWQ-GVM8S")
