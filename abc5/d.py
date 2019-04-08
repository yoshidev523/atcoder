# coding: utf-8
import re
from datetime import datetime as dt
N = input()
D = [[] for j in range(N)]
for i in range(N):
    D[i] = map(int, raw_input().split())
Q = input()
P = []
for i in range(Q):
    P.append(input())

for p in P:
    
