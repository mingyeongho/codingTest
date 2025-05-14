import sys

input = sys.stdin.readline

while True:
  sentence = input().rstrip()
  if sentence == '.':
    break
  brackets = []
  for s in sentence:
    if s == '(' or s == '[':
      brackets.append(s)
    elif s == ')':
      if brackets and brackets[-1] == '(':
        brackets.pop()
      else:
        print("no")
        break
    elif s == ']':
      if brackets and brackets[-1] == '[':
        brackets.pop()
      else:
        print("no")
        break
    elif s == '.':
      print('yes' if len(brackets) == 0 else 'no')
      break