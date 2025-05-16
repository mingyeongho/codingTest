import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dex = dict()
i = 1
for _ in range(n):
  pokemon = input().rstrip()
  dex[pokemon] = i
  dex[str(i)] = pokemon
  i += 1

for _ in range(m):
  k = input().rstrip()
  print(dex[k])