import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(w, h, graph):
    sang = deque([])
    fire = deque([])

    sang_dist = [[-1] * w for _ in range(h)]
    fire_dist = [[-1] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                sang.append((i, j))
                sang_dist[i][j] = 0
            elif graph[i][j] == '*':
                fire.append((i, j))
                fire_dist[i][j] = 0

    while fire:
        xp, yp = fire.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if fire_dist[nx][ny] == -1 and graph[nx][ny] != '#':
                fire_dist[nx][ny] = fire_dist[xp][yp] + 1
                fire.append((nx, ny))

    while sang:
        xp, yp = sang.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < h and 0 <= ny < w):
                return sang_dist[xp][yp] + 1
            if fire_dist[nx][ny] != -1 and fire_dist[nx][ny] <= sang_dist[xp][yp] + 1:
                continue
            if sang_dist[nx][ny] == -1 and graph[nx][ny] == '.':
                sang_dist[nx][ny] = sang_dist[xp][yp] + 1
                sang.append((nx, ny))

    return "IMPOSSIBLE"


for _ in range(t):
    w, h = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]

    print(bfs(w, h, graph))
