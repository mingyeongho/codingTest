import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())  # m: 세로, n: 가로, k: 사각형 개수

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
graph = [[True] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for _ in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            graph[i][j] = False


def bfs(x, y) -> int:
    queue = deque([(x, y)])
    area = 1
    visited[x][y] = True
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                area += 1
    return area


count = 0
sizes = []
for i in range(m):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            area = bfs(i, j)
            sizes.append(area)
            count += 1

sizes.sort()
print(count)
print(*sizes)
