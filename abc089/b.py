import re
import sys

if __name__ == '__main__':
    N = int(input())
    li = raw_input().split()
    d = dict()
    for l in li:
        d[l] = 1
    if len(d) == 4:
        print 'Four'
    else:
        print 'Three'
