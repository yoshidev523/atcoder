# coding: utf-8
import re
from datetime import datetime as dt
if __name == '__main__':
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
    
