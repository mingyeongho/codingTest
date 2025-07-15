import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


def bfs(graph, start):
    dist = [-1] * (N+1)
    dist[start] = 0
    queue = deque([start])
    while queue:
        xp = queue.popleft()
        for nxt in graph[xp]:
            if dist[nxt] == -1:
                dist[nxt] = dist[xp] + 1
                queue.append(nxt)
    return sum(dist) + 1


count = float("inf")
answer = 0

for i in range(1, N+1):
    total = bfs(graph, i)
    if total < count:
        count = total
        answer = i

print(answer)
