Level: Gold5

> [!question] Question
> 세 개의 장대가 있을 때 첫번째 장대에 있는 원판을 세번째 장대에 모두 옮겨야 한다.

> [!success] How?

> [!info] Think
> n번 원판을 3번 장대에 옮기려면 n-1번 까지의 원판들이 모두 2번 장대에 있어야 함.
>
> n개의 원판을 기둥 a에서 기둥 b로 옮기려면
>
> 1. n-1개의 원판을 기둥 a에서 기둥 6-a-b로 옮긴다.
> 2. 원판 n을 기둥 a에서 기둥 b로 옮긴다.
> 3. n-1개의 원판을 기둥 6-a-b에서 기둥 b로 옮긴다.
>
> 횟수는 $2^n - 1$번

> [!tip] Time Complexity
