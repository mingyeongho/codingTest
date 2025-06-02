import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
map = [list(map(int, input().rstrip())) for _ in range(n)]

count = 0
list = []
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * n for _ in range(n)]


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    while queue:
        xp, yp = queue.popleft()
        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny]:
                continue
            if map[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt


for i in range(n):
    for j in range(n):
        if map[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j)
            list.append(cnt)
            count += 1

print(count)
list.sort()
print(*list, sep='\n')
