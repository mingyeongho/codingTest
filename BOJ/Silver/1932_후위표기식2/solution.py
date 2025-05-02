import sys
input = sys.stdin.readline

op = ['+', '-', '*', '/']
defaultOrd = ord("A")

n = int(input().strip())
ex = input().strip() # 후위 표기식
values = [int(input().strip()) for _ in range(n)] # A~Z 값
stack = [values[ord(ex[0]) - defaultOrd], values[ord(ex[1]) - defaultOrd]] # 피연산자를 모아놓는 공간 (값으로 모아놓아야 함)

for i in range(2, len(ex)):
    if ex[i] in op:
        y = stack.pop()
        x = stack.pop()
        if ex[i] == '+':
            stack.append(x + y)
        elif ex[i] == '-':
            stack.append(x - y)
        elif ex[i] == '*':
            stack.append(x * y)
        else:
            stack.append(x / y)
    else:
        stack.append(values[ord(ex[i]) - defaultOrd])

print(f"{stack.pop():.2f}")