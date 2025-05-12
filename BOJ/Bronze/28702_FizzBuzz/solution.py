import sys
input = sys.stdin.readline

data = [input().strip() for _ in range(3)]

def getFizzBuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0 and n % 5 != 0:
        return "Fizz"
    elif n % 3 != 0 and n % 5 == 0:
        return "Buzz"
    else:
        return n

i = 0
while i < 3:
    if data[i].isdecimal():
        break
    else:
        i += 1

if i == 0:
    print(getFizzBuzz(int(data[i]) + 3))
elif i == 1:
    print(getFizzBuzz(int(data[i]) + 2))
elif i == 2:
    print(getFizzBuzz(int(data[i]) + 1))
else:
    print("Fizz")