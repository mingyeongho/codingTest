# Time: 36ms

import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = [tuple(map(int, input().split())) for _ in range(n)]
ans = [0] * n

for i in range(n):
    count = 1
    for j in range(n):
        if i == j:
            continue
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    ans[i] = count

print(*ans)