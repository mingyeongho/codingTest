import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(graph, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


result = []
for _ in range(t):
    m, n, k = map(int, input().split())  # m: 가로, n: 세로, k: 배추의 개수

    graph = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        i, j = map(int, input().split())
        graph[j][i] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(graph, i, j, visited)
                count += 1
    result.append(count)
print(*result, sep='\n')
