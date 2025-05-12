# Time: 40ms

import sys, math
input = sys.stdin.readline

n = int(input().strip())
fac = str(math.factorial(n))
count = 0
for i in range(len(fac) - 1, 0, -1):
    if fac[i] == '0':
        count += 1
    else:
        break
print(count)