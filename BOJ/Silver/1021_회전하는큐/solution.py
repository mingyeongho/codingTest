import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def solution(n, m, nums):
  queue = deque(range(1, n + 1))
  count = 0
  for num in nums:
    if num == queue[0]:
      queue.popleft()
    else:
      idx = queue.index(num)
      if idx > len(queue) // 2:
        queue.rotate(len(queue) - idx)
        count += len(queue) - idx
      else:
        queue.rotate(-idx)
        count += idx
      queue.popleft()
  return count


print(solution(n, m, nums))
