import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
queue = deque([i for i in range(n, 0, -1)])

while len(queue) > 1:
    queue.pop()
    queue.rotate(1)
print(queue[0])
