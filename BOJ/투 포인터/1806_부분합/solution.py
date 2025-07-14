import sys
input = sys.stdin.readline

N, S = map(int, input().split())
seq = list(map(int, input().split()))

en = 0
total = seq[0]
count = float("inf")

for st in range(N):
    while en < N and total < S:
        en += 1
        if en == N:
            break
        total += seq[en]
    if en == N:
        break
    count = min(count, en - st + 1)
    total -= seq[st]

print(count if count != float("inf") else 0)
