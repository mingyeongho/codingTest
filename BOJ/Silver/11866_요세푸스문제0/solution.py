import sys

input = sys.stdin.readline

n, k = map(int, input().split())

datas = [i for i in range(1, n + 1)]
stack = []
idx = 0

while datas:
  idx = (idx + k - 1) % len(datas)
  stack.append(datas.pop(idx))

print(f"<{', '.join(map(str, stack))}>")
