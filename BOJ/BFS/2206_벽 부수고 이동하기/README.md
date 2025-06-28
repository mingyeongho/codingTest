Level: Gold3

> [!question] Question
> N×M의 행렬
> 맵에서 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽이 있는 곳
> (1, 1)에서 (N, M)의 위치까지 이동
> 최단 경로로 이동
> 시작하는 칸과 끝나는 칸도 포함해서 센다.
>  이동하는 도중에 한 개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면, 벽을 한 개 까지 부수고 이동하여도 된다.
>  최단 거리를 출력한다. 불가능할 때는 -1을 출력

> [!success] How?
> 벽을 부술 수 없다고 하면 2d array의 visited 배열을 만들면 됨.
> 벽을 부술 수 있다 -> 3d array의 visited 배열

> [!info] Think
> 3d array로 벽을 부술 때의 visited를 만들 수 있다.

> [!tip] Time Complexity
