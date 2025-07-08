import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alphabets = input().split()
alphabets.sort()

key = [''] * L
has_vowel = False


def backtrack(k, start):
    global has_vowel
    if k == L:
        v_count, c_count = 0, 0
        for k in key:
            if k in ['a', 'e', 'i', 'o', 'u']:
                v_count += 1
            else:
                c_count += 1
        if v_count > 0 and c_count > 1:
            print(''.join(key))
        return

    for i in range(start, C):
        key[k] = alphabets[i]
        backtrack(k+1, i+1)


backtrack(0, 0)
