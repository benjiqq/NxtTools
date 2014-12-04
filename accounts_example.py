"""
accounts example
"""

from nxtapi import *

def get_Account(accountID):
    j = req("getAccount",account=accountID)
    return j
    

someAccount = "10105875265190846103"
print 'balance ',get_Account(someAccount)['balanceNQT']


"""
python accounts_example.py 
{u'unconfirmedBalanceNQT': u'700000000', u'forgedBalanceNQT': u'2142400000000', u'balanceNQT': u'700000000', u'accountRS': u'NXT-QRNR-2CR3-HKZ4-AAUHS', u'publicKey': u'015772aead6002e8ca65663df03d90daee0e3c4d3cecc637ae34fb273fc2fb55', u'requestProcessingTime': 15, u'account': u'10105875265190846103', u'effectiveBalanceNXT': 7, u'guaranteedBalanceNQT': u'700000000'}
"""
