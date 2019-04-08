import re
import sys

if __name__ == '__main__':
    q = input()
    query = []
    for i in range(q):
        a,b = map(int,raw_input().split())
        query.append((a,b))
    for q in query:
        score = q[0] * q[1]
        count = 0
        if q[0] != 1:
            count += 1
        a = 2
        b = score / a
        while a <= b:
            if a != q[0] and b != q[1] and a * b <= score:
                count += 1
            a += 1
            b = score / a
        if q[1] != 1:
            count += 1
        b = 2
        while a > b:
            if a != q[0] and b != q[1] and a * b <= score:
                count += 1
            b += 1
            a = score / b
        print count
