import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ans = [0] * M


def backtrack(k, start):  # k 번째 인덱스에 값을 채우는 함수, start 보다 큰 수가 들어와야 한다.
    if k == M:
        print(*ans)
        return
    for i in range(start, N+1):
        ans[k] = i
        backtrack(k+1, i+1)


backtrack(0, 1)
