import sys

input = sys.stdin.readline

n = int(input().rstrip())
datas = []
for _ in range(n):
  x = int(input().rstrip())
  if x == 0:
    datas.pop()
  else:
    datas.append(x)
print(sum(datas))