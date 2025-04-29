# Time: 36ms, Memory: 34536KB
from math import lcm
import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))