import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[-1] * m for _ in range(n)] for _ in range(k + 1)]  # z, x, y, dist
visited[0][0][0] = 1
queue = deque([(0, 0, 0, 1)])  # z, x, y, dist

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    zp, xp, yp, dp = queue.popleft()
    if xp == n - 1 and yp == m - 1:
        print(dp)
        exit(0)
    is_day = dp % 2
    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if graph[nx][ny] == 0 and visited[zp][nx][ny] == -1:
            visited[zp][nx][ny] = dp + 1
            queue.append((zp, nx, ny, dp + 1))
        if graph[nx][ny] == 1 and zp < k and visited[zp + 1][nx][ny] == -1:
            if is_day:
                visited[zp + 1][nx][ny] = dp + 1
                queue.append((zp + 1, nx, ny, dp + 1))
            else:
                queue.append((zp, xp, yp, dp + 1))

print(-1)
