import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())

direction = [(-2, 1), (-1, 2), (1, 2), (2, 1),
             (2, -1), (1, -2), (-1, -2), (-2, -1)]
result = []
for _ in range(t):
    i = int(input().strip())
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())

    dist = [[-1] * i for _ in range(i)]
    dist[start_x][start_y] = 0
    queue = deque([(start_x, start_y)])
    while queue:
        xp, yp = queue.popleft()
        if xp == end_x and yp == end_y:
            print(dist[xp][yp])
            break
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < i and 0 <= ny < i):
                continue
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[xp][yp] + 1
                queue.append((nx, ny))
