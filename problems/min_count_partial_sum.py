# coding: utf-8
# 最小個数部分和問題
n = input()
A = []
for i in range(n):
    A.append(input())
N = input()
INF = 2**31

#dp[i+1][j]: i番目までの整数の中からいくつかの整数を選んで総和がjとする方法を全て考えた時の選んだ整数の個数の最小値
dp = [[INF for i in range(N+1)] for j in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(N + 1):
        dp[i+1][j] = min(dp[i][j-A[i]]+1, dp[i][j]) if A[i] <= j else dp[i][j]

print dp[n][N] if dp[n][N] != INF else -1
