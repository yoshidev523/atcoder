# coding: utf-8
import re
from datetime import datetime as dt
if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    r = map(int, raw_input().split())
    r.sort()
    r = r[-k:]
    a = 0.0
    for b in r:
        a = float(a + b) / 2
    print a
