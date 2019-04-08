import re
import sys

if __name__ == '__main__':
    H,W,D = map(int, raw_input().split())
    A = dict()
    for i in range(H):
        a = map(int, raw_input().split())
        for j in range(W):
            A[str(a[j])] = (i+1, j+1)
    D = dict()
    for i in range(H*W):
        D[]
    Q = input()
    L = []
    R = []
    for i in range(Q):
        l,r = map(int, raw_input().split())
        L.append(l)
        R.append(r)
    for q in range(Q):
        start = L[q]
        end = R[q]
        now = start
        cost = 0
        while now != end:
            cost += abs(A[str(now)][0] - A[str(now+D)][0]) + abs(A[str(now)][1] - A[str(now+D)][1])
            now += D
        print cost
