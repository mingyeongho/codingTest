import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(n)]


visited = [[[False] * n for _ in range(n)] for _ in range(100 + 1)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, r, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if not visited[nx][ny] and graph[nx][ny] > r:
                queue.append((nx, ny))
                visited[nx][ny] = True


mx = 0
for i in range(100 + 1):  # 비의 양
    count = 0
    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and not visited[i][j][k]:
                bfs(graph, i, j, k, visited[i])
                count += 1
    mx = max(count, mx)
print(mx)
