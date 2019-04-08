# coding: utf-8
import re
from datetime import datetime as dt
if __name__ == '__main__':
    n = input()
    sum = 0.0
    for i in range(n):
        x, u = raw_input().split()
        if u == 'JPY':
            sum += int(x)
        else:
            sum += float(x) * 380000
    print sum
