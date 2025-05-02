import sys
input = sys.stdin.readline

n = int(input().strip())
arr = list(map(int, input().split()))

ngf = [-1] * n
count = [0] * 1_000_001
stack = [0] # 인덱스

for i in arr:
    count[i] += 1

for i in range(1, n):
    while stack and count[arr[stack[-1]]] < count[arr[i]]:
        ngf[stack.pop()] = arr[i]
    stack.append(i)

print(*ngf)