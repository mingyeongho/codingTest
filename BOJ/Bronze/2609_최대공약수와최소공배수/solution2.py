# Time: 40ms, Memory: 34536KB
import sys
from math import gcd, lcm
input = sys.stdin.readline

a, b = map(int, input().split())

print(gcd(a, b))
print(lcm(a, b))