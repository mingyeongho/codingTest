import sys
input = sys.stdin.readline

n = int(input().rstrip())


def isStrfry(original, remake):
    o_alphabets = [0] * 26
    r_alphabets = [0] * 26
    for o in original:
        o_alphabets[ord(o) - ord('a')] += 1
    for r in remake:
        r_alphabets[ord(r) - ord('a')] += 1
    for i in range(26):
        if o_alphabets[i] != r_alphabets[i]:
            return "Impossible"
    return "Possible"


for _ in range(n):
    original, remake = input().split()
    print(isStrfry(original, remake))
