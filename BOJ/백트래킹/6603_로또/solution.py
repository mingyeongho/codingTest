import sys
input = sys.stdin.readline


while True:
    k, *lottos = map(int, input().split())
    if k == 0:
        break
    ans = [0] * 6

    def backtrack(x, start):
        if x == 6:
            print(*ans)
            return
        for i in range(start, k):
            ans[x] = lottos[i]
            backtrack(x+1, i+1)

    backtrack(0, 0)
    print()
