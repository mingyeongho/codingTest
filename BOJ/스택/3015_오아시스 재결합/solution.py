import sys
input = sys.stdin.readline


n = int(input().strip())
heights = [int(input().strip()) for _ in range(n)]

stk = []
answer = 0

for h in heights:
    count = 1

    while stk and stk[-1][0] <= h:
        top_h, top_c = stk.pop()
        answer += top_c
        if top_h == h:
            count += top_c

    if stk:
        answer += 1

    stk.append((h, count))

print(answer)
