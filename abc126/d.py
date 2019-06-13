# coding: utf-8
import re
import bisect
from datetime import datetime as dt
N = input()
color = [-1 for i in range(N)]

M = []
for i in range(N-1):
    M.append(map(int, raw_input().split()))
while len(M) != 0:
    for i, m in M:
        v = m[0]
        u = m[1]
        w = m[2]
        if w % 2 == 0:
            if color[u - 1] != -1:
                color[v - 1] = color[u - 1]
            elif color[v - 1] != -1:
                color[u - 1] = color[v - 1]
            else:
                color[u - 1] = 0
                color[v - 1] = 0
        else:
            if color[u - 1] != -1:
                color[v - 1] = (color[u - 1] + 1) % 2
            elif color[v - 1] != -1:
                color[u - 1] = (color[v - 1] + 1) % 2
        if color[v - 1] != -1 or color[u - 1] != -1:
            M.pop(i)

for i in color:
    print str(i)
