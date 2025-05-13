# Time: 1416ms
# Memory: 48036KB

import sys
input = sys.stdin.readline

n = int(input().strip())
data = [0] * (2_000_000 + 2)

for _ in range(n):
    x = int(input().strip())
    data[x + 1_000_000] += 1

for i in range(len(data)):
    for j in range(data[i]):
        print(i - 1_000_000)