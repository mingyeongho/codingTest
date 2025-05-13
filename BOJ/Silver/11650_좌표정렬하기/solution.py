# Time: 352ms

import sys
input = sys.stdin.readline

n = int(input().rstrip())
points = [tuple(map(int, input().split())) for _ in range(n)]
points = sorted(points, key=lambda point: (point[0], point[1]))

for x, y in points:
    print(x, y)