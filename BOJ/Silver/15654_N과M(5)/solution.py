import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

ans = [0] * m
isUsed = [False] * (10_000 + 1)


def backtrack(k):
    if k == m:
        print(*ans, sep=' ')
        return
    for i in nums:
        if not isUsed[i]:
            ans[k] = i
            isUsed[i] = True
            backtrack(k + 1)
            isUsed[i] = False


backtrack(0)
