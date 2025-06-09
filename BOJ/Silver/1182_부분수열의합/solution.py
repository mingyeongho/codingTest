import sys

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

count = 0


def backtrack(k, total):
    if k == n:
        if total == s:
            global count
            count += 1
        return
    backtrack(k+1, total)
    backtrack(k+1, total+nums[k])


backtrack(0, 0)
print(count-1 if s == 0 else count)
