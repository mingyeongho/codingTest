# 제곱근을 사용한 풀이, Time: 3348ms, Memory: 32412KB
import sys
input = sys.stdin.readline

def isPrimeNumber(num: int) -> bool:
    if num == 1:
        return False
    if num == 2 or num == 3 or num == 5 or num == 7:
        return True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False;
    return True

m, n = map(int, input().split())

for num in range(m, n + 1):
    if isPrimeNumber(num):
        print(num)