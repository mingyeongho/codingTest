import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())
data = [int(input().rstrip()) for _ in range(n)]


# 최빈값
# 최빈값이 여러개라면 두번째로 작은 값을 출력한다.
def mode(data):
  count = [0] * (8_000 + 2)

  for d in data:
    count[d + 4000] += 1

  mv, mc = 0, 0
  same = False

  for iv, ic in enumerate(count):
    if mc < ic:
      mc = ic
      mv = iv - 4000
      same = False
    elif not same and mc == ic:
      same = True
      mv = iv - 4000
  return mv


def solution(data, n):
  data.sort()

  print(math.floor(sum(data) / n + 0.5))  # 산술평균
  print(data[n // 2])  # 중앙값
  print(mode(data)) # 최빈값
  print(max(data) - min(data))  # 범위


solution(data, n)