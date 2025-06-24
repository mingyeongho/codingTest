import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist = [[0] * m for _ in range(n)]


def bfs(graph):
    queue = deque([(0, 0)])
    dist[0][0] = 1
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] == 0 or dist[nx][ny] != 0:
                continue
            queue.append((nx, ny))
            dist[nx][ny] = dist[xp][yp] + 1


bfs(graph)
print(dist[n-1][m-1])
