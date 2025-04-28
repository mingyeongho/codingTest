import sys
input = sys.stdin.readline

def solution(values: str) -> str:
    arr = list(map(int, values.split()))
    return f"{min(arr)} {max(arr)}"

n = int(input().rstrip())
values = input().strip()
print(solution(values))

# TestCase
print(solution("20 10 35 30 7")) # 7 35