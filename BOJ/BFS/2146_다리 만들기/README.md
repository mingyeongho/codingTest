Level: Gold3

> [!question] Question
> 가장 짧은 다리를 만들려고 함.

> [!success] How?
> 2개의 BFS를 수행
>
> 1. 섬 라벨링
> 2. 최단 다리 탐색
>    1. 해당 섬의 모든 육지 칸을 큐에 넣고, $dist[x][y] = 0$으로 초기화
>    2. 바다이면서 아직 방문하지 않았으면 1씩 증가
>    3. 다른 섬에 도달하면 최단 거리

> [!info] Think
> 섬 라벨링을 위한 BFS 1번
> 최단 다리 탐색을 위한 BFS 1번

> [!tip] Time Complexity
