import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

ans = [0] * M
res = set()


def backtrack(k):
    if k == M:
        result = ' '.join(map(str, ans))
        res.add(result)
        return
    for i in range(N):
        ans[k] = nums[i]
        backtrack(k+1)


backtrack(0)

res = sorted(res, key=lambda x: list(map(int, x.split())))
for r in res:
    print(r)
