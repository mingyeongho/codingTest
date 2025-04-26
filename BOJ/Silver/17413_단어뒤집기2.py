import sys
input = sys.stdin.readline

sentence = input().rstrip()

stack = []
result = ''
flag = False

for s in sentence:
    if s == '<':
        while stack:
            result += stack.pop()
        stack.append(s)
        flag = True 
    elif s == '>':
        stack.append(s)
        flag = False
        result += ''.join(stack)
        stack = []
    elif s == ' ' and not flag:
        while stack:
            result += stack.pop()
        result += ' '
    else:
        stack.append(s)

while stack:
    result += stack.pop()
    
print(result)