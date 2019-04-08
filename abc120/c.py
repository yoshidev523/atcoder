# coding: utf-8
import re
import bisect
from datetime import datetime as dt

S = raw_input()
print min(S.count('1'), S.count('0')) * 2
