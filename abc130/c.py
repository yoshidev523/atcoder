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
    W, H, x, y = map(float, input().split())
    if x == W / 2.0 and y == H / 2.0:
        print('{0} {1}'.format(W * H / 2.0, 1))
    else:
        print('{0} {1}'.format(W * H / 2.0, 0))
