import sys
from collections import deque

input = sys.stdin.readline

t = int(input().rstrip())


def solution(p, s):
  queue = deque(s[1:-1].split(","))
  error = False
  cnt_r = 0
  for fn in p:
    if fn == 'R':
      cnt_r += 1
    else:
      if not len(queue) or queue[0] == '':
        print("error")
        error = True
        break
      # cnt_r이 홀수라면 뒤집힌 상태에서 popleft
      if cnt_r % 2:
        queue.pop()
      else:  # cnt_r이 짝수라면 원상태에서 popleft
        queue.popleft()
        cnt_r = 0
  if cnt_r % 2:
    queue.reverse()
  if not error:
    print(f"[{','.join(queue)}]")


for _ in range(t):
  p = input().rstrip()
  n = int(input().rstrip())
  s = input().rstrip()

  solution(p, s)
