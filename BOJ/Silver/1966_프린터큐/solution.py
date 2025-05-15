import sys

input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
  x, y = map(int, input().split())  # x: 문서의 개수, y: 찾고자 하는 문서의 위치
  imp = list(map(int, input().split()))  # 중요도 배열

  result = 1
  while imp:
    if imp[0] < max(imp):
      imp.append(imp.pop(0))
    else:
      if y == 0:
        break
      imp.pop(0)
      result += 1
    y = y - 1 if y > 0 else len(imp) - 1
  print(result)