# 배열을 사용한 풀이

import sys

input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))
x = int(input().rstrip())


def solution(nums, x):
  sizes = [0] * 2_000_001
  count = 0
  for num in nums:
    if sizes[x - num]:
      count += 1
    sizes[num] = 1

  return count


print(solution(nums, x))
