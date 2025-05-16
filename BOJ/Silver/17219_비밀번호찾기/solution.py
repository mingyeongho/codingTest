import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dex = dict()

for _ in range(n):
  address, pw = input().split()
  dex[address] = pw

for _ in range(m):
  address = input().rstrip()
  print(dex[address])