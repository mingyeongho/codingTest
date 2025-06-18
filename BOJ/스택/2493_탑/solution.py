import sys
input = sys.stdin.readline

n = int(input().rstrip())
heights = list(map(int, input().split()))

res = [0] * n
stk = []
for i in range(n, 0, -1):
    h = heights.pop()

    while stk and stk[-1][1] <= h:
        res[stk[-1][0] - 1] = i
        stk.pop()

    stk.append((i, h))
print(*res)
