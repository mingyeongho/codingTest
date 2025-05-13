# Time: 208ms

import sys
input = sys.stdin.readline

n = int(input().rstrip())

members = [(int(age), name) for age, name in (input().split() for _ in range(n))]
members = sorted(members, key=lambda x: x[0])

for member in members:
    print(member[0], member[1])