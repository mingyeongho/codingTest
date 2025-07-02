import sys
from collections import deque
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    h, w = map(int, input().split())
    original_map = [list(input().strip()) for _ in range(h)]
    keys = [False] * 26
    keys_input = input().strip()
    if keys_input != '0':
        for key in keys_input:
            keys[ord(key) - ord('a')] = True

    # 외곽 padding
    graph = [['.'] * (w + 2) for _ in range(h + 2)]
    for i in range(h):
        for j in range(w):
            graph[i + 1][j + 1] = original_map[i][j]
    h += 2
    w += 2

    visited = [[False] * w for _ in range(h)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True

    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    door_wait = [deque() for _ in range(26)]
    cnt = 0

    while queue:
        xp, yp = queue.popleft()

        for dx, dy in direction:
            nx, ny = xp + dx, yp + dy
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if visited[nx][ny]:
                continue
            cell = graph[nx][ny]

            if cell == '*':
                continue
            visited[nx][ny] = True

            if cell == '.':
                queue.append((nx, ny))
            elif cell == '$':
                cnt += 1
                queue.append((nx, ny))
            elif 'a' <= cell <= 'z':
                idx = ord(cell) - ord('a')
                if not keys[idx]:
                    keys[idx] = True
                    while door_wait[idx]:
                        queue.append(door_wait[idx].popleft())
                queue.append((nx, ny))
            elif 'A' <= cell <= 'Z':
                idx = ord(cell) - ord('A')
                if keys[idx]:
                    queue.append((nx, ny))
                else:
                    door_wait[idx].append((nx, ny))
    print(cnt)
