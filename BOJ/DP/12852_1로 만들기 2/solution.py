from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
visited = [False] * (n + 1)
prev = [0] * (n + 1)

queue = deque()
queue.append(n)
visited[n] = True

while queue:
    cur = queue.popleft()

    if cur == 1:
        break

    for nxt in [cur // 3, cur // 2, cur - 1]:
        if (cur % 3 == 0 and nxt == cur // 3) or (cur % 2 == 0 and nxt == cur // 2) or nxt == cur - 1:
            if not visited[nxt]:
                visited[nxt] = True
                prev[nxt] = cur
                queue.append(nxt)

# 경로 역추적
path = []
cur = 1
while cur != 0:
    path.append(cur)
    cur = prev[cur]
path.reverse()

print(len(path) - 1)
print(" ".join(map(str, path)))
