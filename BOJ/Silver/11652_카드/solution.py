import sys
input = sys.stdin.readline

n = int(input().rstrip())
num_dict = {}

for _ in range(n):
    num = int(input().rstrip())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

sorted_dict = sorted(num_dict.items(), key=lambda x: (-x[1], x[0]))
print(sorted_dict[0][0])
