import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [0] * M


def backtrack(k):
    if k == M:
        print(*ans)
        return
    for i in range(N):
        ans[k] = nums[i]
        backtrack(k+1)


backtrack(0)
