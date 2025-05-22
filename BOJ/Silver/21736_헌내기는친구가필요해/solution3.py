import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def get_doyeon(graph, n, m):
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 'I':
        return (i, j)
  return (0, 0)


def count_people(graph, x, y, n, m):
  count = 0
  queue = deque([(x, y)])
  graph[x][y] = 'X'

  while queue:
    xp, yp = queue.popleft()
    for dx, dy in direction:
      nx, ny = xp + dx, yp + dy
      if not (0 <= nx < n and 0 <= ny < m):
        continue
      if graph[nx][ny] == 'P':
        count += 1
      if graph[nx][ny] != 'X':
        queue.append((nx, ny))
        graph[nx][ny] = 'X'
  return count


posi_x, posi_y = get_doyeon(graph, n, m)
result = count_people(graph, posi_x, posi_y, n, m)
print('TT' if result == 0 else result)
