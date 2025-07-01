import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

dist = [-1] * 100_001
prev = [-1] * 100_001
queue = deque([n])
dist[n] = 0

while queue:
    np = queue.popleft()
    if np == k:
        print(dist[np])
        path = []
        cur = k
        while cur != -1:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        print(*path)
        break
    for calc in [np-1, np+1, np*2]:
        if not (0 <= calc < 100_001):
            continue
        if dist[calc] == -1:
            dist[calc] = dist[np] + 1
            prev[calc] = np
            queue.append(calc)
