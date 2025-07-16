import sys
input = sys.stdin.readline

N = int(input().strip())
costs = [list(map(int, input().split())) for _ in range(N)]  # RGB 비용

dp = [[-1] * 3 for _ in range(N+1)]
dp[1][0] = costs[0][0]
dp[1][1] = costs[0][1]
dp[1][2] = costs[0][2]

for i in range(2, N+1):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i-1][1], dp[i-1][2]) + costs[i-1][j]
        elif j == 1:
            dp[i][j] = min(dp[i-1][0], dp[i-1][2]) + costs[i-1][j]
        elif j == 2:
            dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + costs[i-1][j]

print(min(dp[N]))
