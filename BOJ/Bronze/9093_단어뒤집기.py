import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    sentence = input().rstrip()

    for word in sentence.split():
        print(word[::-1], end=' ')
    print()