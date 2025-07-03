import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())


def recur(a, b, c):
    if b == 0:
        return 1
    if b == 1:
        return a % c

    if b % 2 == 0:
        tmp = recur(a, b // 2, c)
        return (tmp * tmp) % c
    else:
        return (a * recur(a, b - 1, c)) % c


print(recur(a, b, c))
