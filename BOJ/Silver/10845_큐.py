from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

n = int(input().rstrip())

def runCommand(command: str):
    if command == 'pop':
            print(queue.popleft() if queue else -1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        print(0 if queue else 1)
    elif command == 'front':
        print(queue[0] if queue else -1)
    elif command == 'back':
        print(queue[-1] if queue else -1)
    else:
        value = command.split()[1]
        queue.append(value)

for _ in range(n):
    command = input().rstrip()

    runCommand(command)

# Test Case
# push 1
# push 2
# front
# back
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front

# runCommand('push 1')
# runCommand('push 2')
# runCommand('front') # 1
# runCommand('back') # 2
# runCommand('size') # 2
# runCommand('empty') # 0
# runCommand('pop') # 1
# runCommand('pop') # 2
# runCommand('pop') # -1
# runCommand('size') # 0
# runCommand('empty') # 1
# runCommand('pop') # -1
# runCommand('push 3')
# runCommand('empty') # 0
# runCommand('front') # 3