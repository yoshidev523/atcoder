# coding: utf-8
import re
import bisect
from datetime import datetime as dt

n = input()
A = map(int, raw_input().split())
minus_count = 0
for a in A:
    if a < 0:
        minus_count += 1
ans = 0
for a in A:
    ans += abs(a)
if minus_count % 2 == 0:
    print ans
else:
    m = 10**10
    for a in A:
        if m > abs(a):
            m = abs(a)
    print ans - 2 * m
