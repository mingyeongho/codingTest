# Time: 956ms

import sys

input = sys.stdin.readline

n = int(input().rstrip())

cnt = [0] * (1_000_000 + 1)
cnt[2], cnt[3] = 1, 1

for i in range(4, n + 1):
  d3, d2, m1 = float("inf"), float("inf"), cnt[i - 1] + 1

  if i % 3 == 0:
    d3 = cnt[i//3] + 1

  if i % 2 == 0:
    d2 = cnt[i // 2] + 1
  
  cnt[i] = int(min([d3, d2, m1]))

print(cnt[n])