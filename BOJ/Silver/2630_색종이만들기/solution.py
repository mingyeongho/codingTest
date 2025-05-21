# Time: 44ms

import sys

input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]

colors = [0, 0]  # white, blue


def recur(n, graph, colors):
  # 모두 같은 색상인지 확인
  color = graph[0][0]  # 1은 파란색, 0은 흰색
  flag = True
  for row in graph:
    for c in row:
      if color != c:
        flag = False
        break
  if flag:
    if color:
      colors[1] += 1
    else:
      colors[0] += 1
  else:
    # 4등분하여 재귀 호출
    half = n // 2
    # 왼쪽 위
    recur(half, [row[:half] for row in graph[:half]], colors)
    # 오른쪽 위
    recur(half, [row[half:] for row in graph[:half]], colors)
    # 왼쪽 아래
    recur(half, [row[:half] for row in graph[half:]], colors)
    # 오른쪽 아래
    recur(half, [row[half:] for row in graph[half:]], colors)


recur(n, graph, colors)

print(colors[0])
print(colors[1])
