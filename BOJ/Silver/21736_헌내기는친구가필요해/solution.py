import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0  # 만난 사람 수


def current_doyeon(graph, n, m):
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 'I':
        return [i, j]
  return [0, 0]


def bfs(graph, x, y):
  global count
  queue = deque([(x, y)])
  graph[x][y] = 'X'

  while queue:
    xp, yp = queue.popleft()
    for i in range(4):
      nx = xp + dx[i]
      ny = yp + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      if graph[nx][ny] == 'P':
        count += 1
      if graph[nx][ny] != 'X':
        queue.append((nx, ny))
        graph[nx][ny] = 'X'


# 도연이의 위치를 알아야함.
position = current_doyeon(graph, n, m)
bfs(graph, position[0], position[1])
print('TT' if count == 0 else count)
