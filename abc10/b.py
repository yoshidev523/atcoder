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
    n = int(input())
    arr = map(int, input().split())
    ans = 0
    for a in arr:
        if a % 6 == 2 or a % 6 == 4:
            ans += 1
        elif a % 6 == 5:
            ans += 2
        elif a % 6 == 0:
            ans += 3
    print(ans)
