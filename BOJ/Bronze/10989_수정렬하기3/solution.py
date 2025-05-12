import sys
input = sys.stdin.readline

n = int(input().strip())

count = [0] * 10_001

for _ in range(n):
    val = int(input().strip())
    count[val] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)