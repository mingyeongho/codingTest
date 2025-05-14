import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

datas = [i for i in range(1, n + 1)]
queue = deque(datas)

while len(queue) > 2:
  queue.popleft()
  queue.append(queue.popleft())

if len(queue) == 2:
  queue.popleft()

print(queue[0])