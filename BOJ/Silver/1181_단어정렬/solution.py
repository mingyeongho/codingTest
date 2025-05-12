# Time: 3544ms

import sys
input = sys.stdin.readline

n = int(input().strip())
data = []
ans = [[] for _ in range(51)]

for _ in range(n):
    word = input().strip()
    if word in data:
        continue
    data.append(word)
    ans[len(word)].append(word)

for i in range(1, len(ans)):
    if len(ans[i]) == 1:
        print(*ans[i])
    elif len(ans[i]) > 1:
        for j in sorted(ans[i]):
            print(j)