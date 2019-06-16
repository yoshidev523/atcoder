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
    n, x = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 1
    d = 0
    for l in L:
        d += l
        if x < d:
            break
        ans += 1
    print(ans)
