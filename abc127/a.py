# coding: utf-8
import re
import bisect
from datetime import datetime as dt
A, B = map(int, input().split())
if 6 <= A <= 12:
    print(int(B / 2))
elif A <= 5:
    print(0)
else:
    print(B)
