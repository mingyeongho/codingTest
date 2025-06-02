# O(K * R * C)

import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
map = [list(input().rstrip()) for _ in range(r)]

dist = [[-1] * c for _ in range(r)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ji_pos = deque([])


def bfs(x, y):
    queue = deque([(x, y)])
    dist[x][y] = 1
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if map[nx][ny] == '#':
                continue
            if dist[nx][ny] == -1 or dist[nx][ny] > dist[xp][yp] + 1:
                queue.append((nx, ny))
                dist[nx][ny] = dist[xp][yp] + 1


for i in range(r):
    for j in range(c):
        if map[i][j] == 'F':
            bfs(i, j)
        if map[i][j] == 'J':
            ji_pos.append((i, j))

x, y = ji_pos[0]
dist[x][y] = 1
while ji_pos:
    xp, yp = ji_pos.popleft()
    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < r and 0 <= ny < c):
            print(dist[xp][yp])
            exit(0)
        if map[nx][ny] == '#':
            continue
        if dist[nx][ny] != -1 and dist[nx][ny] <= dist[xp][yp] + 1:
            continue
        dist[nx][ny] = dist[xp][yp] + 1
        ji_pos.append((nx, ny))

print("IMPOSSIBLE")
