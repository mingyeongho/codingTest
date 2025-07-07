import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [0] * M


def backtrack(k, start):
    if k == M:
        print(*ans)
        return
    for i in range(start, N):
        ans[k] = nums[i]
        backtrack(k+1, i+1)


backtrack(0, 0)
