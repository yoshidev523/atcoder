# -*- coding: utf-8 -*-

if __name__ == '__main__':
    N = input()
    n0 = 2
    n1 = 1
    if N == 1:
        print(1)
    else:
        now = 1
        while now != N:
            n = n0 + n1
            n0 = n1
            n1 = n
            now += 1
        print(n)
