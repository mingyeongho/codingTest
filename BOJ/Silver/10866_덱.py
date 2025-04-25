from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip())
queue = deque()

def runCommand(command):
    cmd = command.split()
    match cmd[0]:
        case "push_front":
            return queue.appendleft(cmd[1])
        case 'push_back':
            return queue.append(cmd[1])
        case 'pop_front':
            return print(queue.popleft() if queue else -1)
        case 'pop_back':
            return print(queue.pop() if queue else -1)
        case 'size':
            return print(len(queue))
        case 'empty':
            return print(1 if not queue else 0)
        case 'front':
            return print(queue[0] if queue else -1)
        case 'back':
            return print(queue[-1] if queue else -1)

for _ in range(n):
    command = input().rstrip()
    runCommand(command)

# test case
# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
# pop_front
# size
# empty
# pop_back
# push_front 3
# empty
# front

# runCommand("push_back 1")
# runCommand("push_front 2")
# runCommand("front")
# runCommand("back")
# runCommand("size")
# runCommand("empty")
# runCommand("pop_front")
# runCommand("pop_back")
# runCommand("pop_front")
# runCommand("size")
# runCommand("empty")
# runCommand("pop_back")
# runCommand("push_front 3")
# runCommand("empty")
# runCommand("front")