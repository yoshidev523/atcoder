# coding: utf-8
import re
import bisect
from datetime import datetime as dt

A, B, K = map(int, raw_input().split())
max = max(A, B)
a = []

for i in range(1, max + 1):
    if A % i == 0 and B % i == 0:
        a.append(i)
print a[len(a)-K]
