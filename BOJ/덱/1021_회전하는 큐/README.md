Level: Silver3

> [!question] Question
> 양방향 순환 큐
> 3가지 연산 수행
>
> 1. 첫번째 원소를 뽑아낸다.
> 2. 왼쪽으로 한 칸 이동
> 3. 오른쪽으로 한 칸 이동
>
> 2번, 3번 연산의 최솟값

> [!success] How?
> 첫번째 원소를 뽑아낸다: popleft
> 왼쪽으로 한 칸 이동: rotate(-1)
> 오른쪽으로 한 칸 이동: rotate(1)
>
> 1부터 n을 원소로 가지는 덱이 있을 때
> ⭐️ 내가 뽑으려고 하는 수가 맨 앞에 있어야 한다.
> for 문을 돌면서 현재 찾으려고 하는 값의 인덱스가 len(arr) // 2보다 크다면 len(arr) - idx 만큼 rotate(양수), 아니라면 idx 만큼 rotate(음수)

> [!info] Think
> 어느 방향으로 몇 번 회전해야 하는지

> [!tip] Time Complexity
> $O(MN)$
