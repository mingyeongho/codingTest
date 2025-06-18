Level: Gold5

> [!question] Question
> 다섯 개의 탑이 수직선 상에 일렬로 서있고, 모든 탑에서 왼쪽으로 레이저를 발사
> 어느 탑에서 수신하는지 알아내는 프로그램

> [!success] How?
> 6 9 5 7 4
> heights를 pop
> 4
> stk에는 (idx + 1, height)로 push
> stk이 빌 때까지 stk의 마지막 원소와 비교
> stk의 마지막 원소보다 pop한 값이 더 크다 -> 현재 i의 값이 res[idx]에 들어감
> 아니라면 stk에 추가

> [!info] Think
> 스택에 튜플을 저장할 수 있다는 생각

> [!tip] Time Complexity
> $O(N)$
