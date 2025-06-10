import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()

    if s == '.':
        exit(0)

    stack = []
    enable = True

    for w in s:
        if w == '(' or w == '[':
            stack.append(w)
        elif w == ')':
            if not stack or stack[-1] != '(':
                enable = False
                break
            stack.pop()
        elif w == ']':
            if not stack or stack[-1] != '[':
                enable = False
                break
            stack.pop()
    print("yes" if not stack and enable else 'no')
