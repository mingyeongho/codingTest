Level: Silver2

> [!question] Question
> 레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현
> 쇠막대기의 왼쪽 끝은 여는 괄호, 오른쪽 끝은 닫는 괄호

> [!success] How?
> 닫는 괄호가 나왔을 때 스택의 마지막 원소가 여는 괄호면 레이저라는 뜻
> 여는 괄호가 나오면 스택에 추가
>
> 닫는 괄호가 나왔을 때.
>
> 1. 레이저: 스택의 마지막 원소가 여는 괄호이다.
>    -> 스택 pop
>    -> count += len(stk)
>    -> temp += len(stk)
>    -> stk = []
> 2. 쇠막대기의 끝
>    -> temp -= 1
>    -> count += 1

> [!info] Think
> 쇠막대기의 끝 로직 구현

> [!tip] Time Complexity
> $O(N)$
