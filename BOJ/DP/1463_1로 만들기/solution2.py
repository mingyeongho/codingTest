import sys
input = sys.stdin.readline

N = int(input().strip())

dist = [-1] * (N+1)
dist[1] = 0

for i in range(2, N+1):
    d3, d2, d1 = float("inf"), float("inf"), dist[i-1] + 1

    if i % 3 == 0:
        d3 = dist[i // 3] + 1
    if i % 2 == 0:
        d2 = dist[i // 2] + 1
    dist[i] = min(d3, d2, d1)
print(dist[N])
