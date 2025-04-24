import sys
input = sys.stdin.readline

n = int(input().rstrip())

stack = []

for _ in range(n):
    command = input().rstrip()

    if 'push' in command:
        x = int(command.split()[1])
        stack.append(x)
    elif command == 'pop':
        print(stack.pop() if stack else -1)
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        print(1 if len(stack) == 0 else 0)
    elif command == 'top':
        print(-1 if len(stack) == 0 else stack[-1])