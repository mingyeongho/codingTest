import sys

input = sys.stdin.readline


while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        exit(0)

    nums = nums[1:]

    nums.sort()
    ans = [0] * 6

    def backtrack(k, start):
        if k == 6:
            print(*ans, sep=' ')
            return
        for i in range(start, len(nums)):
            ans[k] = nums[i]
            backtrack(k+1, i+1)

    backtrack(0, 0)
    print()
