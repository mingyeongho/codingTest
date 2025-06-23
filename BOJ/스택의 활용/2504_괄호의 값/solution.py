import sys
input = sys.stdin.readline

bracket = input().strip()

total = 0
multi = 1
stk = []

for i, b in enumerate(bracket):
    if b == '(':
        stk.append(b)
        multi *= 2
    elif b == '[':
        stk.append(b)
        multi *= 3
    elif b == ')':
        if not stk or stk[-1] != '(':
            print(0)
            exit(0)
        if bracket[i-1] == '(':
            total += multi
        multi //= 2
        stk.pop()
    elif b == ']':
        if not stk or stk[-1] != '[':
            print(0)
            exit(0)
        if bracket[i-1] == '[':
            total += multi
        multi //= 3
        stk.pop()

print(0 if stk else total)
