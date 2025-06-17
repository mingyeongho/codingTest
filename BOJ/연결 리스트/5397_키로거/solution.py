import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    raw = input().rstrip()
    head = []
    tail = []
    for r in raw:
        if r == '<':
            if head:
                tail.append(head.pop())
        elif r == '>':
            if tail:
                head.append(tail.pop())
        elif r == '-':
            if head:
                head.pop()
        else:
            head.append(r)
    tail.reverse()
    head.extend(tail)
    print(''.join(head))
