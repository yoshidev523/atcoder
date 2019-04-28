# coding: utf-8
import re
import bisect
from datetime import datetime as dt

a, b, t = map(int, raw_input().split())
d = a
c = 0
while float(a) <= float(t) + 0.5:
    c += b
    a += d
print c
