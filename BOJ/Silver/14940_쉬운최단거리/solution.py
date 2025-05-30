import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny)) 
                graph[nx][ny] = graph[xp][yp] + 1


def getIdx():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                return (i, j)
    return (0, 0)


x, y = getIdx()
bfs(x, y)

for i in range(n):
    for j in range(m):
        print(0 if graph[i][j] == 0 else graph[i][j] - 2, end=" ")
    print()
