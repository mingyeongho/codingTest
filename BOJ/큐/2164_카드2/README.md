Level: Silver4

> [!question] Question
> N이 주어졌을 때, 제일 마지막에 남는 카드를 구하는 프로그램
> 제일 위에 있는 카드를 버리고 그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

> [!success] How?
> n이 입력되면 큐에 n부터 1까지 집어넣음. (1이 제일 위로 오도록)
> pop 수행 후 rotate(1) 수행

> [!info] Think
> rotate 방법 1. rotate() 사용
> rotate 방법 2. appendleft(pop()) 사용

> [!tip] Time Complexity
> $O(N)$
