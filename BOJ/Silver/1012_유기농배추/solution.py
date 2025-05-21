import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(matrix, x, y):
  queue = deque([(x, y)])
  matrix[y][x] = 0

  while queue:
    xp, yp = queue.popleft()
    for i in range(4):
      nx = xp + dx[i]
      ny = yp + dy[i]
      print(f"nx: {nx}, ny: {ny}, matrix size: {len(matrix[0])}x{len(matrix)}")
      if nx < 0 or nx >= len(matrix[0]) or ny < 0 or ny >= len(matrix):
        continue
      if matrix[ny][nx] == 1:
        queue.append((nx, ny))
        matrix[ny][nx] = 0


for _ in range(n):
  x, y, m = map(int, input().split())  # x: 가로, y: 세로, m: 개수
  matrix = [[0] * x for _ in range(y)]  # 가로 x, 세로 y인 행렬
  count = 0
  for _ in range(m):
    i, j = map(int, input().split())  # i: 가로, j: 세로
    matrix[j][i] = 1

  for i in range(x):
    for j in range(y):
      if matrix[j][i] == 1:
        bfs(matrix, i, j)
        count += 1
  print(count)
