# 나누기 사용, Time: 32ms, Memory: 32412KB
import sys
input = sys.stdin.readline

n = int(input().strip())

def isPrimeNumber(num: int) -> bool:
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False;
    return True

count = 0

nums = list(map(int, input().split()))
for num in nums:
    if num < 2:
        continue
    elif num == 2 or num == 3:
        count += 1
    else:
        if isPrimeNumber(num):
            count += 1
print(count)