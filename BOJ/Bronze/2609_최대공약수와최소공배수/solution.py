# Time: 36ms, Memory: 32544KB
import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def gcd(a: int, b: int) -> int:
    if a % b == 0:
        return b
    r = a % b
    return gcd(b, r)

print(gcd(a, b))
print((a * b) // gcd(a, b))