import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * n for _ in range(n)]


def bfs(graph, x, y, visited) -> int:
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if not visited[nx][ny] and graph[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1
    return count


count = 0
areas = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            count += 1
            area = bfs(graph, i, j, visited)
            areas.append(area)
areas.sort()
print(count)
print(*areas, sep='\n')
