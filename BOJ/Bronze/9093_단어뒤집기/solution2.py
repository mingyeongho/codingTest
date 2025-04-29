# 스택을 이용한 방법, Time: 220ms
import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    stack = []
    sentence = input().split()
    for word in sentence:
        tempStack = []
        listWord = list(word)
        while listWord:
            tempStack.append(listWord.pop())
        stack.append(''.join(tempStack))
    print(" ".join(stack))