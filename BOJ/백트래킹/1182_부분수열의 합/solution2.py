import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0


def backtrack(k, total):
    if k == N:
        if total == S:
            global count
            count += 1
        return
    backtrack(k+1, total)
    backtrack(k+1, total + nums[k])


backtrack(0, 0)
print(count-1 if S == 0 else count)
