import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())  # n: 사다리 개수, m: 뱀 개수

dist = [-1] * 101
move = [i for i in range(101)]

for _ in range(n + m):
    x, y = map(int, input().split())
    move[x] = y


def bfs():
    queue = deque([1])
    dist[1] = 0
    while queue:
        x = queue.popleft()
        for i in range(1, 7):
            nx = move[x + i]
            if nx > 100:
                continue
            if nx == 100:
                return dist[x] + 1
            if dist[nx] != -1:
                continue
            queue.append(nx)
            dist[nx] = dist[x] + 1
    return 0


print(bfs())
