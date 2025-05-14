import sys

input = sys.stdin.readline

n = int(input().rstrip())
targets = map(int, input().split())
m = int(input().rstrip())
datas = list(map(int, input().split()))

targetDict = dict()

for target in targets:
  targetDict[target] = targetDict.get(target, 0) + 1

for data in datas:
  print(targetDict.get(data, 0), end=' ')