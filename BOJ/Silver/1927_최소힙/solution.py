# Time: 120ms

import sys
from heapq import heappush, heappop

input = sys.stdin.readline

n = int(input().rstrip())
heap = []
for _ in range(n):
  m = int(input().rstrip())

  if m == 0:
    print(0 if len(heap) == 0 else heappop(heap))
  else:
    heappush(heap, m)
