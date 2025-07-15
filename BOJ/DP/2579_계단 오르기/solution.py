import sys
input = sys.stdin.readline

n = int(input().strip())
stairs = [0] + [int(input().strip()) for _ in range(n)]

dp = [0] * (n+1)

if n == 1:
    print(stairs[1])
elif n == 2:
    print(stairs[1] + stairs[2])
else:
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, n+1):
        dp[i] = max(stairs[i-1] + dp[i-3], dp[i-2]) + stairs[i]

    print(dp[n])
