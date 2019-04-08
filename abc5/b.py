# coding: utf-8
import re
from datetime import datetime as dt
if __name__ == '__main__':
    n = input()
    t = []
    for i in range(n):
        t.append(input())
    print min(t)
