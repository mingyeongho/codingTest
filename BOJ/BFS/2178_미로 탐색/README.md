Level: Silver1

> [!question] Question
> (1, 1)에서 출발하여 (n, m)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 출력하라.

> [!success] How?
> BFS를 사용
> 거리를 나타내는 이차원 배열을 만들어서 $graph[nx][ny]$가 0이거나 $dist[nx][ny]$가 0이 아니면 continue

> [!info] Think
> 거리를 가지는 2차원 배열을 만들거나
> 방문 처리를 위한 2차원 배열을 가지고 로직을 짜야함.

> [!tip] Time Complexity
> $O(N \times M)$
