# coding: utf-8
import re
from datetime import datetime as dt
if __name__ == '__main__':
    n = input()
    sum = 0.0
    for i in range(n+1):
        sum += i * 10000.0 / float(n)
    print sum
