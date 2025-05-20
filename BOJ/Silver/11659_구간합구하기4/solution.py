# Time: 248ms

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))
sum = [0] * (100_000 + 1)
for i in range(len(data)):
  sum[i+1] = sum[i] + data[i]

for _ in range(m):
  s, e = map(int, input().split())
  print(sum[e] - sum[s-1])