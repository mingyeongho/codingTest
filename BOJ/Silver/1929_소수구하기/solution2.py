# 에라토스테네스의 체를 사용한 풀이, Time: 212ms, Memory: 47760KB
import sys
input = sys.stdin.readline

def eratosthenes(n: int):
    isPrime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for composite in range(i * 2, n + 1, i):
                isPrime[composite] = False
    return isPrime

m, n = map(int, input().split())
primeBools = eratosthenes(n)

for i in range(m, n + 1):
    if primeBools[i]:
        print(i)