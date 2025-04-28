import sys
input = sys.stdin.readline

def solution(values: str, v: int) -> int:
    arr = list(map(int, values.split()))
    return arr.count(v)

n = int(input().strip()) # 입력받을 정수의 개수
values = input().strip() # 입력받은 정수를 배열에 담는 로직
v = int(input().strip()) # 찾을 원소의 값
print(solution(values, v))

# 입력받자마자 배열로 만들고 처리할수도 있긴함
# values = list(map(int, input().split()))
# v = int(input().strip())
# print(values.count(v))
