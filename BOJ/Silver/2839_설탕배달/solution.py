# Time: 48ms

import sys
input = sys.stdin.readline

n = int(input().rstrip())

count = 0
while n > 2:
  if n % 5 == 0:
    count += n // 5
    n = 0
    break
  else:
    n -= 3
    count += 1

print(count if n == 0 else -1)