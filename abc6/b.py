# coding: utf-8
import re
from datetime import datetime as dt
n = input()
a=[0 for i in range(10**6+1)]
a[1] = 0
a[2] = 0
a[3] = 1

if n <= 3:
    print a[n]
    exit()
else:
    for i in range(4, n+1):
        a[i] = (a[i-1] + a[i-2] + a[i-3]) % 10007

print a[n]
