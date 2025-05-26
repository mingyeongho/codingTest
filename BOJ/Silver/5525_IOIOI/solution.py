import sys

input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
s = input().rstrip()


def count_pattern(n, m, s):
  count = 0
  result = 0
  i = 1

  while i < m - 1:
    if s[i - 1:i + 2] == "IOI":
      count += 1
      if count == n:
        result += 1
        count -= 1
      i += 2
    else:
      i += 1
      count = 0
  return result


print(count_pattern(n, m, s))
