import sys
input = sys.stdin.readline

n, x = map(int, input().split()) # n: 입력받을 수열의 개수, x: 조건에 넣을 수
values = list(map(int, input().split()))

for value in values:
    if value < x:
        print(value, end=" ")

