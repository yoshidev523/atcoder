# coding: utf-8
import re
import bisect
from datetime import datetime as dt

n = input()
v = map(int, raw_input().split())
c = map(int, raw_input().split())

ans = 0
for i in range(len(v)):
    if v[i] - c[i] > 0:
        ans += v[i] - c[i]
print ans
