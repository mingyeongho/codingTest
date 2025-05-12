import sys
input = sys.stdin.readline

def fac(n):
    if n <= 1:
        return 1
    return n * fac(n-1)

n, k = map(int, input().split())
print(fac(n) // (fac(n - k) * fac(k)))