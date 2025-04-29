# 리스트 슬라이싱을 이용한 방법, Time: 72ms
import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    reversed = [word[::-1] for word in input().split()]
    print(" ".join(reversed))