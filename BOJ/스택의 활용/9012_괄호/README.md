Level: Silver4

> [!question] Question
> 괄호의 모양이 바르게 구성된 문자열을 VPS라고 한다.
> 주어진 문자열이 VPS인지 판별하는 프로그램

> [!success] How?
> 열린 괄호는 스택에 추가
> 닫힌 괄호는 스택이 존재하지 않다면 에러
> 스택이 존재하고 스택의 마지막 원소가 열린 괄호일 때 pop
> 스택이 존재하고 스택의 마지막 원소가 닫힌 괄호일 때 에러
> 순회가 끝나고 스택에 원소가 남아있으면 에러

> [!info] Think

> [!tip] Time Complexity
> $O(NB)$
