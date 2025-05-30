import sys

input = sys.stdin.readline

dp = [0, 1, 2]

for i in range(3, 1001):
  dp.append(dp[i-1] + dp[i-2])

n = int(input().rstrip())
print(dp[n] % 10_007)