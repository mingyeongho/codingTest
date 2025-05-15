import sys
import math

input = sys.stdin.readline


def solution(list, percentage):
  slice = math.floor(len(list) * ((percentage / 2) / 100) + 0.5)
  list.sort()
  slicedList = list[slice:len(list) - slice]
  avg = math.floor(sum(slicedList) / len(slicedList) + 0.5)
  print(avg)


n = int(input().rstrip())

data = [int(input().rstrip()) for _ in range(n)]

if n == 0:
  print(0)
else:
  solution(data, 30)