# coding: utf-8
if __name__ == '__main__':
    xa, ya, xb, yb, xc, yc = map(int, raw_input().split())
    xb -= xa
    xc -= xa
    yb -= ya
    yc -= ya
    print float(abs(xb*yc - yb*xc)) / 2.0
