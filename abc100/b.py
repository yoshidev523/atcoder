# coding: utf-8
import re
import bisect
from datetime import datetime as dt
import bisect
import math
import sys
input = sys.stdin.readline

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
    d, n = map(int, input().split())
    if n == 100:
        print(100 ** d * (n+1))
    else:
        print(100 ** d * n)
    
