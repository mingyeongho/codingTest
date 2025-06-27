import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[1] * n for _ in range(m)]

for _ in range(k):
    l_x, l_y, r_x, r_y = map(int, input().split())
    for i in range(l_y, r_y):
        for j in range(l_x, r_x):
            graph[i][j] = -1

visited = [[False] * n for _ in range(m)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < m and 0 <= ny < n):
                continue
            if visited[nx][ny]:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count


areas = []
count = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            area = bfs(graph, i, j, visited)
            areas.append(area)

print(count)
areas.sort()
print(*areas)
