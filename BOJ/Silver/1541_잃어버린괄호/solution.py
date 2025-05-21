import sys

input = sys.stdin.readline

exp_list = input().split("-")
sum = 0
for num in exp_list[0].split("+"):
  sum += int(num)

for exp in exp_list[1:]:
  num_list = exp.split("+")
  temp = 0
  for num in num_list:
    temp += int(num)
  sum -= temp
print(sum)
