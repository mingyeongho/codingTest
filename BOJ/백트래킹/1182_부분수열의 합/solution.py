import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

count = 0
ans = []
is_used = [False] * (N+1)


def backtrack(k, start):
    global count

    if k and sum(k) == S:
        count += 1
    if len(k) == N:
        return
    for i in range(start, N):
        if not is_used[i]:
            ans.append(nums[i])
            is_used[i] = True
            backtrack(ans, i+1)
            ans.pop()
            is_used[i] = False


backtrack(ans, 0)

print(count)
