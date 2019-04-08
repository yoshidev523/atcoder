# coding: utf-8
import re
import bisect
from datetime import datetime as dt

N, Q = map(int, raw_input().split())
S = raw_input()
S += ' '
l = []
r = []
for i in range(Q):
    a = map(int, raw_input().split())
    l.append(a[0])
    r.append(a[1])

count = 0
d = [0 for i in range(N+1)]
for i in range(N):
    if S[i]+S[i+1] == 'AC':
        count += 1
    d[i + 1] = count

for i in range(Q):
    print '{}'.format(d[r[i]-1] - d[l[i]-1])
