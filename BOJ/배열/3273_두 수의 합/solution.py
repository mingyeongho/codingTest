import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))
x = int(input().rstrip())

arr = [False] * 1_000_001
count = 0

for num in nums:
    if x - num < 1_000_001 and arr[x - num]:
        count += 1
    arr[num] = True

print(count)
