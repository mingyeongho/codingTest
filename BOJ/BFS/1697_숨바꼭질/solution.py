import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

time = [-1] * 100_001
time[n] = 0

queue = deque([n])
while queue:
    p = queue.popleft()
    if p == k:
        print(time[p])
        exit(0)
    for m in [p-1, p+1, p*2]:
        if not (0 <= m < 100_001):
            continue
        if time[m] == -1:
            time[m] = time[p] + 1
            queue.append(m)
