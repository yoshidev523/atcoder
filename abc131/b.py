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
    n, l = map(int, input().split())
    MIN = l
    MAX = l + n - 1
    ans = l * n + n * (n - 1) / 2
    if MIN >= 0:
        print(int(ans - l))
    elif MIN < 0 and 0 < MAX:
        print(int(ans))
    else:
        print(int(ans - MAX))
