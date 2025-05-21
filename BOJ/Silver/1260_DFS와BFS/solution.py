# Time: 64ms

import sys
from collections import deque

input = sys.stdin.readline


def dfs(graph, v, visited):
  visited[v] = True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)


def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    s = queue.popleft()
    print(s, end=' ')
    for i in graph[s]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True


n, e, s = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
for row in graph:
  row.sort()
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs(graph, s, visited_dfs)
print()
bfs(graph, s, visited_bfs)
