import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split())
grade = [[0, 0] for _ in range(7)]
for _ in range(n):
    s, g = map(int, input().split())
    grade[g][s] += 1

count = 0
for g in grade:
    count += math.ceil(g[0] / k) + math.ceil(g[1] / k)
print(count)
