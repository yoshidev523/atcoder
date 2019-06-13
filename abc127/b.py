# coding: utf-8
import re
import bisect
from datetime import datetime as dt
r, D, X = map(int, input().split())
for i in range(10):
    X = r*X - D
    print(X)
