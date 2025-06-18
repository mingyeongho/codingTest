Level: Silver4

> [!question] Question
> 1부터 N까지 있을 때 K번째 사람을 제거.

> [!success] How?
> 덱을 사용해서 rotate를 왼쪽으로 k번 수행 후 popleft() 수행
> popleft된 값은 배열에 저장 후 출력

> [!info] Think
> rotate(양수)는 오른쪽 회전
> rotate(음수)는 왼쪽 회전

> [!tip] Time Complexity
> $O(NK)$
