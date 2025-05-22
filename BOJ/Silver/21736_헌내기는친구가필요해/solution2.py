import sys
from collections import deque
from typing import List, Tuple

input = sys.stdin.readline

# 상수 정의
EMPTY = 'O'
WALL = 'X'
PERSON = 'P'
DOYEON = 'I'

# 방향 벡터 (상하좌우)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_doyeon_position(campus: List[List[str]], n: int, m: int) -> Tuple[int, int]:
    """도연이의 위치를 찾는 함수"""
    for i in range(n):
        for j in range(m):
            if campus[i][j] == DOYEON:
                return (i, j)
    return (0, 0)

def count_met_people(campus: List[List[str]], start_x: int, start_y: int, n: int, m: int) -> int:
    """BFS를 사용하여 만난 사람의 수를 계산하는 함수"""
    queue = deque([(start_x, start_y)])
    campus[start_x][start_y] = WALL
    people_count = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < n and 0 <= ny < m):
                continue
                
            if campus[nx][ny] == PERSON:
                people_count += 1
            if campus[nx][ny] != WALL:
                queue.append((nx, ny))
                campus[nx][ny] = WALL
                
    return people_count

def main():
    n, m = map(int, input().split())
    campus = [list(input().rstrip()) for _ in range(n)]
    
    doyeon_x, doyeon_y = find_doyeon_position(campus, n, m)
    result = count_met_people(campus, doyeon_x, doyeon_y, n, m)
    
    print('TT' if result == 0 else result)

if __name__ == "__main__":
    main()
