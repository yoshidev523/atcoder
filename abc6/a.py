# coding: utf-8
import re
from datetime import datetime as dt
N = raw_input()
print 'YES' if '3' in N or int(N) % 3 == 0 else 'NO'
