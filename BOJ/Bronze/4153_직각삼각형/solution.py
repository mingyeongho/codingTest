import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == b and b == c and a == 0:
        break

    a, b, c = list(sorted([a, b, c]))

    if (a**2 + b**2) == c**2:
        print("right")
    else:
        print("wrong")