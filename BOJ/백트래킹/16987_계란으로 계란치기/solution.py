import sys
input = sys.stdin.readline

N = int(input().strip())
eggs = [list(map(int, input().split())) for _ in range(N)]

mx_count = 0


def backtrack(k):  # k: 현재 손에 들고 있는 k번째 계란
    global mx_count

    if k == N:
        broken = sum(1 for d, _ in eggs if d <= 0)
        mx_count = max(mx_count, broken)
        return

    if eggs[k][0] <= 0:  # k번째 계란이 이미 깨져있다면 다음 계란을 탐색
        backtrack(k+1)
        return

    hit = False  # 현재 계란으로 다른 계란을 친 적이 있는지 여부
    for i in range(N):
        if i == k or eggs[i][0] <= 0:
            continue
        eggs[k][0] -= eggs[i][1]
        eggs[i][0] -= eggs[k][1]
        hit = True
        backtrack(k+1)
        eggs[k][0] += eggs[i][1]
        eggs[i][0] += eggs[k][1]

    if not hit:
        backtrack(k+1)


backtrack(0)
print(mx_count)
