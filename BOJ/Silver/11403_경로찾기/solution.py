import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * n for _ in range(n)]


def bfs(x):
    queue = deque([x])
    while queue:
        xp = queue.popleft()
        for i in range(len(graph[xp])):
            if graph[xp][i] and not result[x][i]:
                queue.append(i)
                result[x][i] = 1


for i in range(n):
    bfs(i)

for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()
