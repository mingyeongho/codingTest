Level: Silver2

> [!question] Question
> 입력한 키가 주어졌을 때, 비밀번호를 알아내는 프로그램
> 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표
> 백스페이스를 입력하면 -
> 커서 움직임 가능 <>
> 나머지 문자는 비밀번호의 일부

> [!success] How?
> head와 tail 두 배열을 만듦 -를 확인하면 head.pop
> <를 확인하면 tail.append(head.pop())
> .>를 확인하면 head.append(tail.pop())
> 나머지는 head.append()

> [!info] Think

> [!tip] Time Complexity
> $O(L), L은 문자열의 길이$
