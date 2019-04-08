# coding: utf-8
import re
import bisect
from datetime import datetime as dt

S = raw_input()
i = 0
max = 0
tmp = 0
while i < len(S):
    if S[i] in 'ACGT':
        tmp += 1
    else:
        if max < tmp:
            max = tmp
        tmp = 0
    i += 1
if max < tmp:
    max = tmp
print max
