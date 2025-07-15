import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

dist = [-1] * (N + 1)
dist[N] = 0

queue = deque([N])
while queue:
    xp = queue.popleft()
    if xp == 1:
        break
    for res in [xp/3, xp/2, xp-1]:
        if int(res) != res:
            continue
        res = int(res)
        if dist[res] == -1:
            dist[res] = dist[xp] + 1
            queue.append(res)

print(dist[1])
