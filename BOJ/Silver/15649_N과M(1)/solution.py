import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
ans = [0] * m
isUsed = [False] * (n+1)


def backtrack(k):
    if k == m:
        for i in range(m):
            print(ans[i], end=' ')
        print()
        return
    for i in range(1, n+1):
        if not isUsed[i]:
            ans[k] = i
            isUsed[i] = True
            backtrack(k + 1)
            isUsed[i] = False


backtrack(0)
