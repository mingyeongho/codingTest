import sys
input = sys.stdin.readline

n = int(input().strip())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    a, b = 1, 2  # a = dp[i-2], b = dp[i-1]
    for _ in range(3, n + 1):
        a, b = b, (a + b) % 10_007
    print(b)
