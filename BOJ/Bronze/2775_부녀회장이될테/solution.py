import sys, math
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    k = int(input().strip())
    n = int(input().strip())

    dp = [[0] * 15 for _ in range(15)]

    # 0층 채우기
    for i in range(1, 15):
        dp[0][i] = i

    # 1호 채우기
    for i in range(1, 15):
        dp[i][1] = 1

    # dp 채우기
    for i in range(1, 15):
        for j in range(2, 15):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    print(dp[k][n])