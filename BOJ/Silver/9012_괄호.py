import sys
input = sys.stdin.readline


# def isVps(s: str) -> bool:
#     queue = deque()
#     for i in range(len(s)):
#         queue.append(s[i])
#         if queue[0] == '(' and queue[-1] == ')':
#             queue.popleft()
#             queue.pop()
#     return True if len(queue) == 0 else False

def isVps(s: str) -> bool:
    try:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            else:
                stack.pop()
        return True if len(stack) == 0 else False
    except:
        return False

n = int(input().rstrip())
for _ in range(n):
    s = input().rstrip()
    print("YES" if isVps(s) else "NO")