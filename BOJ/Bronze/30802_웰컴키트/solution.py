import sys, math
input = sys.stdin.readline

n = int(input().strip())
sizes = list(map(int, input().split())) # s, m, l, xl, xxl, xxxl
t, p = map(int, input().split())

tCount = 0

for size in sizes:
    if size == 0:
        continue

    if size % t == 0:
        tCount += size // t
    else:
        tCount += size // t + 1

print(tCount)
print(n // p, n % p)