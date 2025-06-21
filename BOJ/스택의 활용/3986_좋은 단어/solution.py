import sys
input = sys.stdin.readline

n = int(input().strip())

count = 0


def solution(s) -> bool:
    stk = []
    for w in s:
        if stk and stk[-1] == w:
            stk.pop()
        else:
            stk.append(w)
    return False if stk else True


for i in range(n):
    s = input().strip()
    if solution(s):
        count += 1

print(count)
