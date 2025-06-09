import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ans = [0] * m


def backtrack(k):
    if k == m:
        print(*ans, sep=" ")
        return
    for i in range(1, n + 1):
        ans[k] = i
        backtrack(k + 1)


backtrack(0)
