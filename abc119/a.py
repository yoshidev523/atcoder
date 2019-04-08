# coding: utf-8
import re
from datetime import datetime as dt
if __name__ == '__main__':
    s = dt.strptime(raw_input(), '%Y/%m/%d')
    a = dt(2019, 4, 30, 0, 0,0)
    if (s - a).days <= 0:
        print 'Heisei'
    else:
        print 'TBD'
