# Time: 76ms

import sys
input = sys.stdin.readline

n = int(input().strip())
data = [input().strip() for _ in range(n)]
data = list(set(data))

for a in sorted(data, key=lambda s: (len(s), s)):
    print(a)