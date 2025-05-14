# Time: 96ms

import sys
input = sys.stdin.readline

N = 8

wRow = 'WBWBWBWB'
bRow = 'BWBWBWBW'
wBoard = [wRow, bRow, wRow, bRow, wRow, bRow, wRow, bRow]
bBoard = [bRow, wRow, bRow, wRow, bRow, wRow, bRow, wRow]

m, n = map(int, input().split())
board = [input().strip() for _ in range(m)]

minCount = float('inf')
for i in range(m - N + 1):
    for j in range(n - N + 1):
        count = 0
        for p in range(N):
            for q in range(N):
                if board[i + p][j + q] != wBoard[p][q]:
                    count += 1
        minCount = min(minCount, count)
        count = 0
        for p in range(N):
            for q in range(N):
                if board[i + p][j + q] != bBoard[p][q]:
                    count += 1
        minCount = min(minCount, count)
print(minCount)