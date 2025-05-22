import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

count = 0
visited = [False] * (n + 1)


def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


while False in visited[1:]:
  # visited[1:]에서 처음 False가 나오는 인덱스가 start
  start = visited[1:].index(False) + 1
  bfs(graph, start, visited)
  count += 1

print(count)
