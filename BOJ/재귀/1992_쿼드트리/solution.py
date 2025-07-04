import sys
input = sys.stdin.readline

N = int(input().strip())
graph = [list(map(int, input().strip())) for _ in range(N)]


def recur(x, y, n) -> str:
    color = graph[x][y]
    same = True

    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != color:
                same = False
                break
        if not same:
            break

    if same:
        print(color, end='')
    else:
        new_n = n // 2
        print("(", end='')
        for i in [0, new_n]:
            for j in [0, new_n]:
                recur(x+i, y+j, new_n)
        print(")", end='')


recur(0, 0, N)
