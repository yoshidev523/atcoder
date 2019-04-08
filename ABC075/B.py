# -*- coding: utf-8 -*-

def count(S,i,j):
    if i >= 0 and i < H and j >= 0 and j < W:
        if S[i][j] != '#':
            S[i][j] += 1

H, W = map(int, raw_input().split())
S = [['' for i in range(W)] for j in range(H)]
mine = []
for h in range(H):
    tmps = raw_input()
    for index,tmp in enumerate(tmps):
        if tmp == '#':
            S[h][index] = '#'
        else:
            S[h][index] = 0
for i,a in enumerate(S):
    for j,b in enumerate(a):
        if b == '#':
            count(S,i,j+1)
            count(S,i,j-1)
            count(S,i-1,j-1)
            count(S,i-1,j)
            count(S,i-1,j+1)
            count(S,i+1,j-1)
            count(S,i+1,j)
            count(S,i+1,j+1)
for s in S:
    p = ''
    for q in s:
        p = p + str(q)
    print(p)
