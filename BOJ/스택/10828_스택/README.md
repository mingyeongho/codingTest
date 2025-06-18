Level: Silver4

> [!question] Question
> 정수를 저장하는 스택을 구현
> push X: 정수 X를 스택에 넣는 연산
> pop: 가장 뒤에 있는 정수를 제거 후 출력. 스택이 비어있으면 -1 출력
> size: 스택에 들어있는 정수의 개수 출력
> empty: 스택이 비어있으면 1, 아니면 0
> top: 스택의 가장 뒤에 있는 정수 출력. 스택이 비어있으면 -1 출력

> [!success] How?
> push X: append
> pop: if stk: pop else: -1
> size: len
> empty: if stk: 0 else: 1
> top: if stk: stk[-1] else: -1

> [!info] Think
> print(-1 if not stk else stk.pop()) 이런식으로 사용하면 코드 길이를 줄일 수 있음

> [!tip] Time Complexity
