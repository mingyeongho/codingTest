import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())


# 2^N x 2^N 배열에서 (r, c)를 방문하는 순서를 반환하는 함수
def recur(N, r, c):
    if N == 0:
        return 0
    # 재귀식: (r, c)가 어느 사분면에 있느냐에 따라 식이 달라짐.
    half = 1 << (N - 1)
    if r < half and c < half:
        return recur(N-1, r, c)
    elif r < half and c >= half:
        return half * half + recur(N-1, r, c - half)
    elif r >= half and c < half:
        return 2 * half * half + recur(N-1, r-half, c)
    else:
        return 3 * half * half + recur(N-1, r-half, c-half)


print(recur(N, r, c))
