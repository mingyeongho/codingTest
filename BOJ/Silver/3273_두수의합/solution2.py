# 투 포인터를 사용한 풀이

import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))
x = int(input().rstrip())

nums.sort()


def solution(nums, n, x):
  count = 0
  st = 0
  en = n - 1
  while st < en:
    if nums[st] + nums[en] == x:
      count += 1
      st += 1
      en -= 1
    elif nums[st] + nums[en] < x:
      st += 1
    else:
      en -= 1
  return count


print(solution(nums, n, x))
