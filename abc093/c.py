import re
import sys

if __name__ == '__main__':
    l = map(int, raw_input().split())
    l.sort()
    count = 0
    while l[2] != l[1] or l[1] != l[0]:
        while l[0] == l[1]:
            count += 1
            l[0] += 1
            l[1] += 1
            if l[2] == l[1] and l[1] == l[0]:
                break
        l.sort()
        while l[2] - l[0] > 1:
            count += 1
            l[0] += 2
        if l[2] == l[1] and l[1] == l[0]:
            break
        while l[2] - l[1] > 1:
            count += 1
            l[1] += 2
        if l[2] == l[1] and l[1] == l[0]:
            break
        l.sort()
        if l[1] == l[2]:
            count += 1
            l[0] += 2

    print count
