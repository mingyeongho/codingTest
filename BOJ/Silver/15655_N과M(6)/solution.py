import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

ans = [0] * m


def backtrack(k, start):
    if k == m:
        print(*ans, sep=' ')
        return
    for i in range(start, n):
        ans[k] = nums[i]
        backtrack(k+1, i+1)


backtrack(0, 0)
