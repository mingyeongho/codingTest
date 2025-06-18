import sys
input = sys.stdin.readline

n = int(input().rstrip())

val = 1
stk = []
res_stk = []
for _ in range(n):
    m = int(input().rstrip())

    if m >= val:
        while val <= m:
            res_stk.append('+')
            stk.append(val)
            val += 1
        res_stk.append('-')
        stk.pop()
    else:  # m이 val보다 작다
        if stk and stk[-1] == m:
            res_stk.append('-')
            stk.pop()
        else:
            print("NO")
            exit(0)
print(*res_stk, sep='\n')
