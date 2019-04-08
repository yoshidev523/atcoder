# coding: utf-8
import re
from datetime import datetime as dt
N, M = map(int, raw_input().split())
for z in range(N + 1):
    x = 3 * N - M + z
    y = M - 2 * N - 2 * z
    if x >= 0 and y >= 0:
        print x, y, z
        exit()
print '-1 -1 -1'
