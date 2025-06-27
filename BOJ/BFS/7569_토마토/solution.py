import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())  # m: 가로, n: 세로, h: 높이
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dist = [[[-1] * m for _ in range(n)] for _ in range(h)]
direction = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
             (0, -1, 0), (0, 0, -1), (0, 0, 1)]

queue = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))
                dist[i][j][k] = 0

while queue:
    zp, xp, yp = queue.popleft()
    for dz, dx, dy in direction:
        nz, nx, ny = zp + dz, xp + dx, yp + dy
        if not (0 <= nz < h and 0 <= nx < n and 0 <= ny < m):
            continue
        if graph[nz][nx][ny] == 0 and dist[nz][nx][ny] == -1:
            queue.append((nz, nx, ny))
            dist[nz][nx][ny] = dist[zp][xp][yp] + 1

mx = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if dist[i][j][k] == -1 and graph[i][j][k] == 0:
                print(-1)
                exit(0)
            mx = max(mx, dist[i][j][k])
print(mx)
