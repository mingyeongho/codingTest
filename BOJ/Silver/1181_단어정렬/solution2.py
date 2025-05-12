# Time: 3556ms

import sys
input = sys.stdin.readline

n = int(input().strip())
data = []

for _ in range(n):
    word = input().strip()
    if word in data:
        continue
    data.append(word)

for a in sorted(data, key=lambda s: (len(s), s)):
    print(a)