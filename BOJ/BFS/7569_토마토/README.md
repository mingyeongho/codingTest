Level: Gold5

> [!question] Question
> 3d 배열에서 토마토가 모두 익으려면 최소 며칠이 걸리는지
> 모두 익지 못하는 상황은 -1 출력

> [!success] How?
> `[[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]` 3d 입력 받기

> [!info] Think
> 입력을 3d로 받도록 해야함.
> direction도 3방향으로
> 나머지는 일반 BFS 처럼

> [!tip] Time Complexity
