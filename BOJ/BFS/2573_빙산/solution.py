import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

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
            if not visited[nx][ny] and graph[nx][ny] > 0:
                queue.append((nx, ny))
                visited[nx][ny] += 1


def count_iceberg(graph) -> int:
    count = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and not visited[i][j]:
                bfs(graph, i, j, visited)
                count += 1
    return count


year = 0
while True:
    year += 1
    # 빙산 근처의 바다 개수
    melt = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                cnt = 0
                for dx, dy in direction:
                    nx, ny = i + dx, j + dy
                    if not (0 <= nx < n and 0 <= ny < m):
                        continue
                    if graph[nx][ny] == 0:
                        cnt += 1
                melt[i][j] = cnt

    is_ice_exist = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                graph[i][j] = max(0, graph[i][j] - melt[i][j])
                if graph[i][j] > 0:
                    is_ice_exist = True

    if not is_ice_exist:
        print(0)
        break

    count = count_iceberg(graph)
    if count >= 2:
        print(year)
        break
