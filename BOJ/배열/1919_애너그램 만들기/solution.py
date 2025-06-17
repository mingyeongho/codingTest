import sys
input = sys.stdin.readline

a, b = [input().rstrip() for _ in range(2)]

a_alphabets = [0] * 26
b_alphabets = [0] * 26

for i in a:
    a_alphabets[ord(i) - ord('a')] += 1
for i in b:
    b_alphabets[ord(i) - ord('a')] += 1

count = 0
for i in range(26):
    count += abs(a_alphabets[i] - b_alphabets[i])
print(count)
