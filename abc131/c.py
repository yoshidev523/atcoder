# coding: utf-8
import re
import bisect
from datetime import datetime as dt
import bisect
import fractions

def gcd(a, b):
    return int(fractions.gcd(a, b))

def lcm(a, b):
    return int(a * b // gcd(a, b))

def calc(n, a, b):
    return int(n//a + n//b - n//lcm(a,b))

if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))
    ans = calc(b, c, d) - calc(a - 1, c, d)
    print(b - a + 1 - ans)
