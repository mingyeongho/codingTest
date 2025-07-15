import sys
input = sys.stdin.readline

t = int(input().strip())

dp = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0]

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input().strip())
    print(dp[n])
