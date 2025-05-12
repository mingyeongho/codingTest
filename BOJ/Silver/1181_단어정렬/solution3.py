# Time: 68ms

import sys
input = sys.stdin.readline

n = int(input().strip())
words = [input().strip() for _ in range(n)]
words = list(set(words))
words.sort()
words = sorted(words, key=len)

for i in words:
    print(i)