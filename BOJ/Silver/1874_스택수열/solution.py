import sys
input = sys.stdin.readline

n = int(input().strip())

stack, result = [], []
i = 1 # stack에 넣을 값
flag = True # 수열을 만들 수 있는지

for _ in range(n):
    x = int(input().strip())
    
    while i <= x:
        result.append("+")
        stack.append(i)
        i += 1
    
    if x == stack[-1]:
        result.append("-")
        stack.pop()
    else:
        flag = False
        break
print("NO" if not flag else "\n".join(result))