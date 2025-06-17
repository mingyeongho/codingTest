import sys
input = sys.stdin.readline

number = input().rstrip()
count = [0] * 10

for n in number:
    if n == '6' or n == '9':
        if count[6] > count[9]:
            count[9] += 1
        else:
            count[6] += 1
        pass
    else:
        count[int(n)] += 1
print(max(count))
