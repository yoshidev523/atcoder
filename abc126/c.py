# coding: utf-8
import re
import bisect
from datetime import datetime as dt
import math
n, k = map(int, raw_input().split())
X = []
i = 1
while i <= n:
    x = max(math.ceil(math.log((float(k) / float(i)), 2)), 0)
    X.append(2 ** (-int(x)))
    i += 1
print sum(X) * n ** (-1)
