# coding: utf-8
import re
import bisect
from datetime import datetime as dt
S = raw_input()
first = int(S[0]) * 10 + int(S[1])
second = int(S[2]) * 10 + int(S[3])
if 1 <= first <= 12 and 1 <= second <= 12:
    print 'AMBIGUOUS'
elif 1 <= first <= 12:
    print 'MMYY'
elif 1 <= second <= 12:
    print 'YYMM'
else:
    print 'NA'
