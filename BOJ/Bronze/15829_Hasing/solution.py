import sys, math
input = sys.stdin.readline

l = int(input().strip())
val = input().strip()

r = 31
M = 1_234_567_891

sum = 0
for i in range(l):
    num = ord(val[i]) - 96
    sum += num * (r**i)

print(sum % M)