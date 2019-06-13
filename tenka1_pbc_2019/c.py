# coding: utf-8
import re
import bisect
from datetime import datetime as dt
n = input()

s = raw_input()
m = n
left = s[:0].count('#')
right = s[0:].count('.')
m = min(m, left + right)
for i in range(len(s)):
    if s[i] == '.':
        right -= 1
    else:
        left += 1
    m = min(m, right + left)
print m
