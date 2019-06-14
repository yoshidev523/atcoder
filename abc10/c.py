# coding: utf-8
import re
import bisect
from datetime import datetime as dt
import bisect
import math

def gcd(a, b):
    return math.gcd(a, b)

def lcm(a, b):
    return a * b / gcd(a, b)

class slist(list):
    def __init__(self, *args, **kw):
        list.__init__(self, *args, **kw)
        self.sort()

    def append(self, value):
        bisect.insort(self,value)

    def index_left(self, value):
        return bisect.bisect_left(self, value)

if __name__ == '__main__':
    sx, sy, ex, ey, t, v = map(int, input().split())
    n = int(input())
    arr = [None] * n
    for i in range(n):
        arr[i] = list(map(int, input().split()))

    for a in arr:
        dist = float((sx-a[0])**2 + (sy-a[1])**2)**0.5 + float((ex-a[0])**2 + (ey-a[1])**2)**0.5
        if dist <= float(t*v):
            print('YES')
            exit()
    print('NO')
