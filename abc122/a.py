# coding: utf-8
import re
import bisect
from datetime import datetime as dt
b = raw_input()
if b == 'A':
    print 'T'
elif b == 'C':
    print 'G'
elif b == 'G':
    print 'C'
else:
    print 'A'
