import sys
input = sys.stdin.readline

arr = list(input().rstrip()) # 커서 앞의 문자열
tail = [] # 커서 뒤의 문자열

n = int(input().rstrip())

for _ in range(n):
    command = input().rstrip()

    if command == 'L': # 커서를 왼쪽으로 한 칸 이동
        if arr:
            tail.append(arr.pop())
    elif command == 'D': # 커서를 오른쪽으로 한 칸 이동
        if tail:
            arr.append(tail.pop())
    elif command == 'B': # 커서 왼쪽에 있는 문자를 삭제
        if arr:
            arr.pop()
    else: # P $, 커서 왼쪽에 $ 문자를 추가
        word = command.split()[1]
        arr.append(word)

arr.extend(reversed(tail))
print("".join(arr))