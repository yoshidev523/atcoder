# coding: utf-8
import re
import bisect
from datetime import datetime as dt
import bisect
import math

# INF = 10 ** 11
if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    sum = [0]*(N+1)
    for idx, a in enumerate(A):
        sum[idx + 1] = sum[idx] + a
    ans = 0
    for idx, a in enumerate(A):
        target = sum[idx] + K
        # print(sum[idx:N+1])
        # print(target)
        i = bisect.bisect_left(sum, target)
        # print(i)
        ans+=N-i+1

    print(ans)
