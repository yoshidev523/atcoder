# coding: utf-8
import re
import bisect
from datetime import datetime as dt
N, M = map(int, raw_input().split())
route = []
for i in range(M):
    route.append(int, raw_input().split())
dp = [[0 for i in range(N + 1)] fo j in range(M + 1)]
for i in range(N):
    for j in range(M + 1):
        dp[i+1]
