# coding: utf-8

n = input()
A = []
for i in range(n):
    A.append(input())
N = input()

# dp[i+1][j]: i番目までの整数の中からいくつか選んで総和をjとすることが可能かどうが（boolean）
dp = [[0 for i in range(N + 1)] for j in range(n + 1)]

for i in range(N + 1):
    if i == 0:
        dp[0][i] = True
    else:
        dp[0][i] = False

for i in range(n):
    for j in range(N + 1):
        if A[i] <= j:
            dp[i+1][j] = dp[i][j-A[i]] or dp[i][j]
        else:
            dp[i+1][j] = dp[i][j]

print dp[n][N]
