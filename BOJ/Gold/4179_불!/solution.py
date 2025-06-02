# O(R * C)

import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
map = [list(input().rstrip()) for _ in range(r)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 거리 배열: 불, 지훈이 각각
dist_fire = [[-1] * c for _ in range(r)]
dist_ji = [[-1] * c for _ in range(r)]

fire_queue = deque()
ji_queue = deque()

for i in range(r):
    for j in range(c):
        if map[i][j] == 'F':
            fire_queue.append((i, j))
            dist_fire[i][j] = 0
        elif map[i][j] == 'J':
            ji_queue.append((i, j))
            dist_ji[i][j] = 0

# 불 확산 BFS
while fire_queue:
    x, y = fire_queue.popleft()
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if map[nx][ny] != '#' and dist_fire[nx][ny] == -1:
                dist_fire[nx][ny] = dist_fire[x][y] + 1
                fire_queue.append((nx, ny))

# 지훈이 이동 BFS
while ji_queue:
    x, y = ji_queue.popleft()
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        # 범위 벗어나면 탈출
        if not (0 <= nx < r and 0 <= ny < c):
            print(dist_ji[x][y] + 1)
            exit(0)
        if map[nx][ny] == '#' or dist_ji[nx][ny] != -1:
            continue
        # 불이 이미 번진 곳이거나, 불이 더 빨리 도착하는 곳은 못 감
        if dist_fire[nx][ny] != -1 and dist_fire[nx][ny] <= dist_ji[x][y] + 1:
            continue
        dist_ji[nx][ny] = dist_ji[x][y] + 1
        ji_queue.append((nx, ny))

print("IMPOSSIBLE")
