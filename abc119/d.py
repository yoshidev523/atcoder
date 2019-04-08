# coding: utf-8
import re
from datetime import datetime as dt

def yoshi_code():
    a, b, q = map(int, raw_input().split())
    s = []
    t = []
    x = []
    for i in range(a):
        s.append(input())
    for i in range(b):
        t.append(input())
    for i in range(q):
        x.append(input())

    for i in x:
        te = b - 1
        sh = a - 1
        for j in range(a):
            if i < s[j]:
                sh = j
                break
        for j in range(b):
            if i < t[j]:
                te = j
                break
        if sh == 0:
            sh_array = [sh]
        elif sh == len(s) - 1 and i > s[sh]:
            sh_array = [sh]
        else:
            sh_array = [sh-1, sh]
        if te == 0:
            te_array = [te]
        elif te == len(t) - 1 and i > t[te]:
            te_array = [te]
        else:
            te_array = [te-1, te]
        min = abs(i-s[sh]) + abs(s[sh] - t[te])
        for j in sh_array:
            for k in te_array:
                if min > abs(i-s[j]) + abs(s[j]-t[k]):
                    min = abs(i-s[j]) + abs(s[j]-t[k])
        for j in te_array:
            for k in sh_array:
                if min > abs(i-t[j]) + abs(t[j]-s[k]):
                    min = abs(i-t[j]) + abs(t[j]-s[k])
        print min
N, A, B, C = map(int, raw_input().split())
l = [int(input()) for in range(N)]
INF = 10 ** 9

def dfs(cur, a, b, c):
    if cur == N:
        return abs(a-A) + abs(b-B) + abs(c-C) - 30 if min(a, b, c) > 0 else INF
    ret0 = dfs(cur + 1, a, b, c)
    ret1 = dfs(cur + 1, a + 1[cur], b, c) + 10
    ret2 = dfs(cur + 1, a, b + 1[cur], c) + 10
    ret3 = dfs(cur + 1, a, b, c + 1[cur]) + 10
    return min(ret0, ret1, ret2, ret3)
if __name__ == '__main__':
    print dfs(0, 0, 0, 0)
