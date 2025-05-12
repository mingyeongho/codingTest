# Time: 64ms

import sys
input = sys.stdin.readline

n = int(input().strip())
data = [input().strip() for _ in range(n)]
data = list(set(data))
data.sort()

for a in sorted(data, key=len):
    print(a)