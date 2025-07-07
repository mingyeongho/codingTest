import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ans = [0] * M  # 수열을 담을 배열
is_used = [False] * (N+1)  # 특정 수가 쓰였는지를 확인하는 배열


def backtrack(k):  # k번째 인덱스에 값을 채우는 함수
    if k == M:
        print(*ans)
        return
    for i in range(1, N+1):
        if not is_used[i]:
            ans[k] = i
            is_used[i] = True
            backtrack(k+1)
            is_used[i] = False


backtrack(0)
