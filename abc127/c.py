# coding: utf-8
import re
import bisect
from datetime import datetime as dt
n, m = map(int, input().split())
L = []
R = []
for i in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
maxL = max(L)
minR = min(R)
print(max(0, minR - maxL + 1))
