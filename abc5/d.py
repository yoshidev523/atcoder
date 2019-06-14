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
    
