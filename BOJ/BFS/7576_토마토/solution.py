import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())  # m: 가로, n: 세로
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    xp, yp = queue.popleft()
    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if graph[nx][ny] == 0:
            queue.append((nx, ny))
            graph[nx][ny] = graph[xp][yp] + 1

max_day = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        max_day = max(graph[i][j], max_day)
print(max_day-1)
