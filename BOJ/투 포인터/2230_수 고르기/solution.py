import sys
input = sys.stdin.readline

N, M = map(int, input().split())
seq = [int(input().strip()) for _ in range(N)]

seq.sort()

en = 0
mn = float("inf")

for st in range(N):
    while en < N and seq[en] - seq[st] < M:
        en += 1
    if en == N:
        break
    mn = min(mn, seq[en] - seq[st])

print(mn)
