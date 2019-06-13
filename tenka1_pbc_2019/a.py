# coding: utf-8
import re
import bisect
from datetime import datetime as dt
A, B, C = map(int, raw_input().split())

if A < C < B or B < C < A:
    print 'Yes'
else:
    print 'No'
