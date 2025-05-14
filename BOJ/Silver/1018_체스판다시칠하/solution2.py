# Time: 60ms

import sys
input = sys.stdin.readline

n , m = map(int, input().split())

board = []
result = []
for i in range(0,n):
    board.append(list(input().strip()))

for y in range(0, n-7):
    for x in range(0, m-7):
        b_count = 0
        w_count = 0
        for i in range(y,y+8):
            for j in range(x, x+8):
                if (i+j)%2 == 0:
                    if board[i][j] == 'W':
                        b_count += 1
                    else:
                        w_count += 1
                else:
                    if board[i][j] == 'W':
                        w_count += 1
                    else:
                        b_count += 1
        result.append(b_count)
        result.append(w_count)

print(min(result))