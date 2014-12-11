"""
blocks
"""

from nxtapi import *

blocks = req("getAccountBlockIds",account="7114946486381367146",lastIndex="0")
print blocks

#{u'requestProcessingTime': 227, u'blockIds': [u'5143527866040770567']}
