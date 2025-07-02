import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
switches = {}
for _ in range(m):
    x, y, a, b = map(int, input().split())
    switches.setdefault((x-1, y-1), []).append((a-1, b-1))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

bright = [[False] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]
bright[0][0] = True
visited[0][0] = True
queue = deque([(0, 0)])

cnt = 1
while queue:
    xp, yp = queue.popleft()

    for bx, by in switches.get((xp, yp), []):
        if not bright[bx][by]:
            bright[bx][by] = True
            cnt += 1
            for dx, dy in direction:
                px, py = bx + dx, by + dy
                if not (0 <= px < n and 0 <= py < n):
                    continue
                if visited[px][py]:
                    visited[bx][by] = True
                    queue.append((bx, by))
                    break

    for dx, dy in direction:
        nx, ny = xp + dx, yp + dy
        if not (0 <= nx < n and 0 <= ny < n):
            continue
        if bright[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny))

print(cnt)
