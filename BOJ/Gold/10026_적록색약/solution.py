import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
paint = [list(input().rstrip()) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited_nrg = [[False] * n for _ in range(n)]
visited_rg = [[False] * n for _ in range(n)]


def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        xp,  yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny]:
                continue
            if paint[nx][ny] == paint[xp][yp]:
                queue.append((nx, ny))
                visited[nx][ny] = True


count_nrg = 0
count_rg = 0
for i in range(n):
    for j in range(n):
        if not visited_nrg[i][j]:
            bfs(i, j, visited_nrg)
            count_nrg += 1

for i in range(n):
    for j in range(n):
        if paint[i][j] == 'R':
            paint[i][j] = 'G'

for i in range(n):
    for j in range(n):
        if not visited_rg[i][j]:
            bfs(i, j, visited_rg)
            count_rg += 1

print(count_nrg, count_rg)
