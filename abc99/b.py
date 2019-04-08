# coding: utf-8
if __name__ == '__main__':
    a,b = map(int, raw_input().split())
    c = b - a - 1
    d = 0
    for i in range(c):
        d += (i + 1)
    print (d - a)
