Level: Silver4

> [!question] Question
> 명령어에 맞는 큐를 구현

> [!success] How?
> deque을 사용해 queue 구현
> push X: append
> pop: popleft 출력, queue가 없으면 -1
> size: len
> empty: if queue
> front: 0번째 인덱스, queue가 없으면 -1
> back: -1번째 인덱스, queue가 없으면 -1

> [!info] Think
> 명령어의 개수가 2,000,000 이하.
> deque을 사용한 구현이라서 명령어들의 시간 복잡도는 $O(1)$

> [!tip] Time Complexity
> 명령어들의 시간 복잡도: $O(1)$
