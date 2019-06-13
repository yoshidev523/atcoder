# coding: utf-8
import re
import bisect
from datetime import datetime as dt

n, m = map(int, input().split())
A = list(map(int, input().split()))
for i in range(m):
    b, c = map(int, input().split())
    for i in range(b):
        A.append(c)
A.sort()
print(sum(A[(len(A)-n):len(A)]))
