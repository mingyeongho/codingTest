Level: Gold5

> [!question] Question
> 높이가 다른 빌딩들이 있을 때
> 관리인이 확인할 수 있는 옥상정원의 총 수

> [!success] How?
> n = 6
> heights = [10, 3, 7, 4, 12, 2] 일 때,
> 10이 확인할 수 있는 옥상 정원: 3
> 3이 확인할 수 있는 옥상 정원: 0
> 7이 확인할 수 있는 옥상 정원: 1
> stk
> count = [0] \* n
> pop을 하면서 시도
> 처음에 2를 확인 -> stk이 비어있음 -> stk에 (6, 2)를 넣음
> 12를 확인 -> stk에 (6, 2)가 들어있음 -> count[5] += 1 -> stk.pop() -> stk.append((5, 12))
> 4를 확인 -> stk에 [(5, 12)]가 들어있음 -> stk에 (4, 4)를 넣음
> 7을 확인 -> stk에 (4, 4)가 들어있음 -> count[3] += 1 -> stk.pop()
>
> 결론. heights를 pop하면서 진행
> h가 stk의 맨 뒤의 원소의 높이보다 크면 count가 1 + count[stk 맨 뒤의 원소의 인덱스]만큼 증가

> [!info] Think

> [!tip] Time Complexity
> $O(N)$
