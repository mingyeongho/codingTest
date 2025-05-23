import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 100_001


def bfs(visited, n, k):
  queue = deque([n])
  visited[n] = 0

  while queue:
    v = queue.popleft()
    if v == k:
      return visited[v]

    for c in [v-1, v+1, v*2]:
      if 0 <= c <= 100_000 and visited[c] == -1:
        visited[c] = visited[v] + 1
        queue.append(c)

print(bfs(visited, n, k))
