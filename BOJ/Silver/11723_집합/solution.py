import sys

input = sys.stdin.readline

n = int(input().rstrip())

s = 0b_0_0000_0000_0000_0000_0000

for _ in range(n):
  cmd = input().split()

  if cmd[0] == 'all':
    s = 0b_1_1111_1111_1111_1111_1111
  elif cmd[0] == 'empty':
    s = 0b_0_0000_0000_0000_0000_0000
  elif cmd[0] == 'add':
    m = int(cmd[1])
    s |= (1 << m)
  elif cmd[0] == 'remove':
    m = int(cmd[1])
    s &= ~(1 << m)
  elif cmd[0] == 'toggle':
    m = int(cmd[1])
    s ^= (1 << m)
  elif cmd[0] == 'check':
    m = int(cmd[1])
    print(1 if s & (1 << m) else 0)
