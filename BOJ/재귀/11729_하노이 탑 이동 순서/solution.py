import sys
input = sys.stdin.readline

n = int(input().strip())

cnt = 0


def recur(a, b, n):  # n개의 원판을 기둥 a에서 기둥 b로 옮기는 함수
    if n == 1:
        print(f"{a} {b}")
        return
    recur(a, 6-a-b, n-1)
    print(a, b)
    recur(6-a-b, b, n-1)


print(2**n - 1)  # (1 << n) - 1
recur(1, 3, n)


'''
n개의 원판을 기둥 a에서 기둥 b로 옮기려면
1. n-1개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다.
2. 원판 n을 기둥 a에서 기둥 b로 옮긴다.
3. n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다.
'''
