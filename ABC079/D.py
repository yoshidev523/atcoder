# -*- coding: utf-8 -*-
H, W = map(int, raw_input().split())
c = [[0 for i in range(10)] for j in range(10)]
A = [[0 for i in range(W)] for j in range(H)]
for i in range(10):
    n = map(int, raw_input().split())
    for j in range(10):
        c[i][j] = n[j]
for i in range(H):
    n = map(int, raw_input().split())
    for j in range(W):
        A[i][j] = n[j]
        
def getDistance(start):
    if start == 1:
        return 0
    d = [1001 for i in range(10)]
    d[start] = 0
    prev = [-1 for i in range(10)]
    Q = set()
    for i in range(10):
        Q.add(i)
    while len(Q) != 0:
        min = 1001
        for i in range(10):
            if d[i] < min and i in Q:
                min = d[i]
                u = i
        Q.remove(u)
        for v in range(10):
            if d[v] > d[u] + c[u][v]:
                d[v] = d[u] + c[u][v]
                prev[v] = u
    return(d[1])



if __name__ == '__main__':
    D = [0 for i in range(10)]
    for i in range(10):
        D[i] = getDistance(i)
        print(D[i])
    ans = 0
    for i in range(H):
        for j in range(W):
            if A[i][j] != -1:
                ans += D[A[i][j]]
    print(ans)
