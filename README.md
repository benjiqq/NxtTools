NxtTools
========

Nxt python tools. simple implemention of HTTP requests to the API. 

## Examples

3 lines of code to get account data

```
from nxtapi import *
someAccount = "10105875265190846103"
print 'balance ',get_Account(someAccount)['balanceNQT']
```

Result
```
python accounts_example.py 
balance  150800000000
```

## Install

only requirement is ```pip install requests```

Nxt node must be running on 127.0.0.1:7876