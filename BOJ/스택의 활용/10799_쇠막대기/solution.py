import sys
input = sys.stdin.readline

b = input().strip()

temp = 0
stk = []
count = 0

for bb in b:
    if bb == '(':
        stk.append(bb)
    else:
        if stk and stk[-1] == '(':  # 레이저
            stk.pop()
            count += len(stk) + temp
            temp += len(stk)
            stk = []
        else:
            temp -= 1
            count += 1
print(count)
