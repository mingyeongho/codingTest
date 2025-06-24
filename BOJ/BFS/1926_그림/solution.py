import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y, visited) -> int:
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 1
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny] or graph[nx][ny] == 0:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
            area += 1
    return area


count = 0  # 그림의 개수
max_area = 0  # 가장 넓은 그림의 넓이
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            area = bfs(graph, i, j, visited)
            max_area = max(area, max_area)

print(count)
print(max_area)
