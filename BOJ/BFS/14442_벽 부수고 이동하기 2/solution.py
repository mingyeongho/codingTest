import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist = [[[-1] * m for _ in range(n)] for _ in range(k+1)]
dist[0][0][0] = 1
queue = deque([(0, 0, 0)])


while queue:
    zp, xp, yp = queue.popleft()
    if xp == n-1 and yp == m-1:
        print(dist[zp][xp][yp])
        exit(0)
    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        # 방문하지 않았으면서 벽을 부술 수 있는 상태면서 벽인 경우
        if zp < k and graph[nx][ny] == 1 and dist[zp+1][nx][ny] == -1:
            dist[zp+1][nx][ny] = dist[zp][xp][yp] + 1
            queue.append((zp+1, nx, ny))
        # 방문하지 않았으면서 이동할 수 있는 공간일 때
        if graph[nx][ny] == 0 and dist[zp][nx][ny] == -1:
            dist[zp][nx][ny] = dist[zp][xp][yp] + 1
            queue.append((zp, nx, ny))
print(-1)
