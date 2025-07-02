import sys
import re
from collections import deque
input = sys.stdin.readline

n, m, p = map(int, input().split())  # n: 세로, m: 가로, p: 사람 수
s_list = [0] + list(map(int, input().split()))  # 각 플레이어가 이동할 수 있는 칸 수
graph = [list(input().strip()) for _ in range(n)]

# 턴마다 플레이어의 순서가 바뀌므로 2중 for문을 돌며 처음 상황을 큐에 넣음
# 1번 플레이어의 턴에서는 1번 플레이어의 모든 성을 확장 <- 큐에 1번 성, 2번 성 이렇게 넣을 수 있어야 함.
seq = [deque() for _ in range(p + 1)]
cnt = [0] * (p + 1)  # 성의 개수
for i in range(n):
    for j in range(m):
        if not re.match(r"[.#]", graph[i][j]):
            pp = int(graph[i][j])
            seq[pp].append((i, j))
            cnt[pp] += 1

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while True:
    is_expanded = False
    for i in range(1, p+1):
        cur_s = s_list[i]
        queue = seq[i]
        if not queue:
            continue
        for _ in range(cur_s):
            nxt = deque()
            while queue:
                xp, yp = queue.popleft()
                for dx, dy in direction:
                    nx, ny = xp + dx, yp + dy
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.':
                        graph[nx][ny] = str(i)
                        nxt.append((nx, ny))
                        cnt[i] += 1
                        is_expanded = True
            if not nxt:
                break
            queue = nxt
        seq[i] = queue
    if not is_expanded:
        break

print(*cnt[1:])
