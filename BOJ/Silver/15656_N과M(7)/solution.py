import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

ans = [0] * m


def backtrack(k):
    if k == m:
        print(*ans, sep=' ')
        return
    for num in nums:
        ans[k] = num
        backtrack(k+1)


backtrack(0)
