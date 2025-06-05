import sys

input = sys.stdin.readline

n, m = map(int, input().split())

ans = [0] * m
isUsed = [False] * (n + 1)


def backtrack(k):
    if k == m:
        print(' '.join(map(str, ans)))
        return
    for i in range(1, n+1):
        if not isUsed[i]:
            ans[k] = i
            for j in range(1, i + 1):
                if not isUsed[j]:
                    isUsed[j] = True
            backtrack(k+1)
            for j in range(1, i + 1):
                isUsed[j] = False


backtrack(0)
