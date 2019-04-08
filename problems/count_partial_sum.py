# coding: utf-8

n = input()
A = []
for i in range(n):
    A.append(input())
N = input()

# dp[i+1][j]: i番目までの整数の中からいくつか選んで総和がjとなる場合の数
dp = [[0 for i in range(N + 1)] for j in range(n + 1)]

MOD = 1000000009
for i in range(N + 1):
    if i == 0:
        dp[0][i] = 1
    else:
        dp[0][i] = 0

for i in range(n):
    for j in range(N + 1):
        if A[i] <= j:
            dp[i+1][j] = (dp[i][j-A[i]] + dp[i][j]) % MOD
        else:
            dp[i+1][j] = dp[i][j] % MOD

print dp[n][N]
