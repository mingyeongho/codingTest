import sys, math
input = sys.stdin.readline

while True:
    n = input().strip()

    if n == '0':
        break
    
    flag = True

    for i in range(len(n) // 2):
        if n[i] != n[-1 - i]:
            flag = False
            break
    if flag:
        print("yes")
    else:
        print("no")