"""
tx.py

NxtAPI example use for transactions
"""

from nxtapi import *

"""
transaction

[u'feeNQT', u'senderPublicKey', u'height', u'ecBlockId', u'deadline', u'ecBlockHeight', u'amountNQT', u'senderRS', u'version', u'attachment', u'type', u'timestamp', u'blockTimestamp', u'fullHash', u'recipient', u'recipientRS', u'transaction', u'sender', u'signatureHash', u'subtype', u'confirmations', u'signature', u'block']
"""

def filter_inputs(txs, acc):
    inputs = list()
    for tx in txs[:]:
        sender = tx['senderRS']
        recp = tx['recipientRS']
        amnt = int(tx['amountNQT'])

        if recp == acc:
            inputs.append(tx)
    return inputs


def filter_outputs(txs, acc):
    inputs = list()
    for tx in txs[:]:
        sender = tx['senderRS']
        recp = tx['recipientRS']
        amnt = int(tx['amountNQT'])

        if sender == acc:
            inputs.append(tx)
    return inputs

def show_inputs(txs, acc):
    print '*'*30
    print 'inputs to ' , acc 
    print '*'*30

    for tx in txs[:]:
        sender = tx['senderRS']
        recp = tx['recipientRS']
        amnt = int(tx['amountNQT'])

        print '%i from %s'%(amnt, sender)


def show_outputs(txs, acc):
    print '*'*30
    print 'outputs from ' , acc 
    print '*'*30

    for tx in txs[:]:
        sender = tx['senderRS']
        recp = tx['recipientRS']
        amnt = int(tx['amountNQT'])

        print '%i to %s'%(amnt, recp)


acc = "NXT-QRNR-2CR3-HKZ4-AAUHS"
txs = get_tx(acc)['transactions']
inputs = filter_inputs(txs,acc)
inputs = inputs[:5]

outputs = filter_outputs(txs,acc)
outputs = outputs[:5]

#print inputs
show_inputs(inputs, acc)
show_outputs(outputs, acc)




