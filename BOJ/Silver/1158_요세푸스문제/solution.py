import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
dq = deque(range(1, n + 1))
result = []

while dq:
  dq.rotate(-(m - 1))
  result.append(dq.popleft())

print(f"<{', '.join(map(str, result))}>")
