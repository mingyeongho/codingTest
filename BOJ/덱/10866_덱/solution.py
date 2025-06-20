import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
queue = deque([])
for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push_front':
        queue.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        queue.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(queue.popleft() if queue else -1)
    elif cmd[0] == 'pop_back':
        print(queue.pop() if queue else -1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        print(0 if queue else 1)
    elif cmd[0] == 'front':
        print(queue[0] if queue else -1)
    elif cmd[0] == 'back':
        print(queue[-1] if queue else -1)
