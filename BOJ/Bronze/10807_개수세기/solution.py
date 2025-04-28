import sys
input = sys.stdin.readline

def solution(values: str, v: int) -> int:
    arr = list(map(int, values.split()))
    count = 0 # 찾을 원소의 개수
    
    for value in arr:
        if value == v:
            count += 1
    
    return count

n = int(input().strip()) # 입력받을 정수의 개수
values = input().strip() # 입력받은 정수를 배열에 담는 로직
v = int(input().strip()) # 찾을 원소의 값
print(solution(values, v))

# TestCase
# print(solution("1 4 1 2 4 2 4 2 3 4 4", 2)) # 3
# print(solution("1 4 1 2 4 2 4 2 3 4 4", 5)) # 0