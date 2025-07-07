import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [0] * M
is_used = [False] * (N+1)


def backtrack(k):
    if k == M:
        print(*ans)
        return
    for i, n in enumerate(nums):
        if not is_used[i]:
            ans[k] = n
            is_used[i] = True
            backtrack(k+1)
            is_used[i] = False


backtrack(0)
