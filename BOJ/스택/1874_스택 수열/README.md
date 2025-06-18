Level: Silver2

> [!question] Question
> 1부터 n까지의 수를 스택에 넣었다가 꺼냄으로써 수열을 만들 수 있다.
> 스택에 push 하는 순서는 무조건 오름차순
> 수열을 만들 수 있는지 없는지 판별하는 프로그램

> [!success] How?
> [], m: 4, val: 1 -> ++++-
> [1,2,3], m: 3 val: 5 -> -
> [1,2], m: 6, val: 5 -> ++-
> [1,2,5], m: 8, val: 7 -> ++-
> 입력된 수가 추가되어야 할 수보다 크거나 같다면 추가 후 제거

> [!info] Think

> [!tip] Time Complexity
