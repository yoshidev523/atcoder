# coding: utf-8
import re
import bisect
from datetime import datetime as dt
A, B, C = map(int, raw_input().split())

print min(B / A, C)
