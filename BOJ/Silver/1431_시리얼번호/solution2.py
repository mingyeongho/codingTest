import sys
input = sys.stdin.readline

n = int(input().rstrip())
numbers = [input().rstrip() for _ in range(n)]


numbers.sort(key=lambda x: (len(x),  sum(int(num)
             for num in x if num.isdecimal()), x))
print(*numbers, sep='\n')
