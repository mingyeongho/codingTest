import sys
input = sys.stdin.readline

n = int(input().rstrip())
numbers = [input().rstrip() for _ in range(n)]
real = []

for number in numbers:
    sum = 0
    for val in number:
        if val.isdecimal():
            sum += int(val)
    real.append((number, sum))


real.sort(key=lambda x: (len(x[0]),  x[1], x[0]))
for num, sum in real:
    print(num)
