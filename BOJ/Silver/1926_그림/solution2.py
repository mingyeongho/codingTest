# use DFS

import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * m for _ in range(n)]
count = 0
mx = 0


def dfs(x, y):
  visited[x][y] = True
  area = 1
  for dx, dy in direction:
    nx, ny = x + dx, y + dy
    if not (0 <= nx < n and 0 <= ny < m):
      continue
    if graph[nx][ny] == 0 or visited[nx][ny]:
      continue
    area += dfs(nx, ny)
  return area


for i in range(n):
  for j in range(m):
    if graph[i][j] == 0 or visited[i][j]:
      continue
    area = dfs(i, j)
    count += 1
    mx = max(mx, area)

print (count)
print(mx)