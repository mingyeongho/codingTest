import sys
input = sys.stdin.readline

n = int(input().strip())


def solution(b) -> bool:
    stk = []
    for bb in b:
        if bb == '(':
            stk.append(bb)
        else:
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                return False
    return True if not stk else False


for _ in range(n):
    b = input().strip()
    print("YES" if solution(b) else "NO")
