# use BFS

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * m for _ in range(n)]
count = 0
mx = 0

def bfs(x, y):
  queue = deque([(x, y)])
  visited[x][y] = True
  area = 1
  while queue:
    xp, yp = queue.popleft()
    for dx, dy in direction:
      nx, ny = xp + dx, yp + dy
      if not (0 <= nx < n and 0 <= ny < m):
        continue
      if not graph[nx][ny] or visited[nx][ny]:
        continue
      queue.append((nx, ny))
      visited[nx][ny] = True
      area += 1
  return area

for i in range(n):
  for j in range(m):
    if graph[i][j] == 0 or visited[i][j]:
      continue
    area = bfs(i, j)
    count += 1
    mx = max(mx, area)

print(count)
print(mx)