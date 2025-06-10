import sys
input = sys.stdin.readline

n = int(input().rstrip())
heights = [int(input().rstrip()) for _ in range(n)]

stack = []
ans = [0] * n

for i in range(n-1, -1, -1):
    h = heights.pop()
    count = 0

    while stack and stack[-1][1] < h:
        count += ans[stack[-1][0]] + 1
        stack.pop()

    ans[i] = count
    stack.append((i, h))

print(sum(ans))
