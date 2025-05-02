# 종나 어렵다
# Time: 1032ms

import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

nge = [-1] * n
stack = [0] # 아직 오큰수를 찾지 못한 인덱스

for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        nge[stack.pop()] = arr[i]
    stack.append(i)

print(*nge)