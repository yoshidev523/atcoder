# coding: utf-8
import re
import bisect
from datetime import datetime as dt
n, k = map(int, raw_input().split())
s = raw_input()
ans = ""
for i, a in enumerate(s):
    if i == k - 1:
        ans += a.lower()
    else:
        ans += a

print(ans)
