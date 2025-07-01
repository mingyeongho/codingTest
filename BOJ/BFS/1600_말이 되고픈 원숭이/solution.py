import sys
from collections import deque
input = sys.stdin.readline

k = int(input().strip())  # 원숭이가 k번 말의 움직임을 따라할 수 있음
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
direction_h = [(-2, 1), (-1, 2), (1, 2), (2, 1),
               (2, -1), (1, -2), (-1, -2), (-2, -1)]
dist = [[[-1] * w for _ in range(h)] for _ in range(k+1)]
dist[0][0][0] = 0
queue = deque([(0, 0, 0)])

while queue:
    zp, xp, yp = queue.popleft()
    if xp == h-1 and yp == w-1:
        print(dist[zp][xp][yp])
        exit(0)

    if zp < k:  # 말처럼 움직일 수 있을 때
        for dx, dy in direction_h:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if graph[nx][ny] == 0 and dist[zp+1][nx][ny] == -1:
                dist[zp+1][nx][ny] = dist[zp][xp][yp] + 1
                queue.append((zp+1, nx, ny))
    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < h and 0 <= ny < w):
            continue
        if dist[zp][nx][ny] == -1 and graph[nx][ny] == 0:
            dist[zp][nx][ny] = dist[zp][xp][yp] + 1
            queue.append((zp, nx, ny))
print(-1)
