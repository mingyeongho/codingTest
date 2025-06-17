import sys
input = sys.stdin.readline

word = input().rstrip()
alphabets = [0] * 26
for alphabet in word:
    alphabets[ord(alphabet)-ord('a')] += 1
print(*alphabets, sep=' ')
