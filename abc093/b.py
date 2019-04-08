import re
import sys

if __name__ == '__main__':
    a,b,k = map(int , raw_input().split())
    l = []
    for i in range(k):
        if a + i <= b:
            print a + i
            l.append(a+i)
    for i in range(k):
        if (b - k + i + 1) not in l and (b - k + i + 1) >= a:
            print b - k + i + 1
