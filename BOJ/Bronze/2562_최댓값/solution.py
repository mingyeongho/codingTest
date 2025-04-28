import sys
input = sys.stdin.readline

values = [int(input().strip()) for _ in range(9)] # 9개의 줄에 입력을 받을 수 있고 그 값을 values에 저장

print(max(values))
print(values.index(max(values)) + 1)