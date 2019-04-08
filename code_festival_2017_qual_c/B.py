# -*- coding: utf-8 -*-
if __name__ == '__main__':
    N = raw_input()
    A = map(int, raw_input().split())
    c_total = 1
    c_odd = 1
    for a in A:
        c_total *= 3
        if a % 2 == 0:
            c_odd *= 2
    print c_total - c_odd
