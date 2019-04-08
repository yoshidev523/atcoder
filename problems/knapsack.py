# coding: utf-8

n = input()
W = []
V = []
for i in range(n):
    a = map(int, raw_input().split())
    W.append(a[0])
    V.append(a[1])
M = input()

# dp[i+1][j]: i番目までの品物の中から重さがjを超えないように選んだ時の価値の総和の最大値
dp = [[0 for i in range(M+1)] for j in range(n+1)]

print dp
for i in range(n):
    for m in range(M+1):
        if m >= W[i]:
            dp[i+1][m]= max(dp[i][m-W[i]] + V[i], dp[i][m])
        else:
            dp[i+1][m] = dp[i][m]

print dp
print dp[n][M]
