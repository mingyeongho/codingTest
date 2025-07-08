import sys
input = sys.stdin.readline

N = int(input().strip())

count = 0
is_used = [False] * N  # 열
is_used_r = [False] * (2*N-1)  # 오른쪽 대각선
is_used_l = [False] * (2*N-1)  # 왼쪽 대각선


def backtrack(k):
    if k == N:
        global count
        count += 1
        return
    for i in range(N):
        if is_used[i] or is_used_r[k-i+N-1] or is_used_l[k+i]:
            continue
        is_used[i] = True
        is_used_r[k-i+N-1] = True
        is_used_l[k+i] = True
        backtrack(k+1)
        is_used[i] = False
        is_used_r[k-i+N-1] = False
        is_used_l[k+i] = False


backtrack(0)
print(count)
