import sys
input = sys.stdin.readline

N = int(input().strip())  # 3의 거듭제곱 (3, 9, 27, ...)

graph = [[False] * N for _ in range(N)]


def recur(x, y, n):
    if n == 1:
        graph[x][y] = True
        return
    new_n = n // 3
    for dx in [0, new_n, 2 * new_n]:
        for dy in [0, new_n, 2 * new_n]:
            if dx == new_n and dy == new_n:
                continue  # 가운데는 비워둠
            recur(x + dx, y + dy, new_n)


recur(0, 0, N)

for row in graph:
    print(''.join('*' if cell else ' ' for cell in row))
