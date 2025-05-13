# Time: 1244ms
# Memory: 97808KB

import sys
input = sys.stdin.readline

n = int(input().strip())
data = [int(input().strip()) for _ in range(n)]
data.sort()
print(*data, sep="\n")