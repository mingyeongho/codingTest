import sys
input = sys.stdin.readline

def solution(values: str, x: int):
    result = [] # 조건에 맞는 수가 추가될 배열
    arr = list(map(int, values.split())) # string to list
    
    for value in arr:
        if value < x:
            result.append(value)
    
    return " ".join(map(str, result))
    
n, x = map(int, input().split()) # n: 입력받을 수열의 개수, x: 조건에 넣을 수
values = input().strip()
print(solution(values, x))

# TestCase
print(solution("1 10 4 9 2 3 8 5 7 6", 5))