import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ans = [0] * M


def backtrack(k):
    if k == M:
        print(*ans)
        return
    for i in range(1, N+1):
        ans[k] = i
        backtrack(k+1)


backtrack(0)
