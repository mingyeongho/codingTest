import sys
input = sys.stdin.readline

n, *nums = input().split()
while len(nums) < int(n):
    nums.extend(input().split())

r_nums = list(map(lambda x: int(x[::-1]), nums))
r_nums.sort()

print(*r_nums, sep='\n')
