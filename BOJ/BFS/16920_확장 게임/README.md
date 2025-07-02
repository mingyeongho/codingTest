Level: Gold2

> [!question] Question
> 자기 턴이 돌아올 때마다 성을 확장.
> 플레이어 i는 자신의 성이 있는 곳에서 $S_i$칸 만큼 이동할 수 있는 모든 칸에 성을 동시에 만듦.
> 벽이나 다른 플레이어의 성이 있는 곳으로는 이동할 수 없다.

> [!success] How?
> 플레이어 별 개별 queue 사용
> BFS를 $S_i$ 만큼 수행
> 확장 체크

> [!info] Think
> 성의 순서대로 큐에 넣어야 함.
> $S_i$칸 만큼 움직일 수 있다 = 위 + 옆 도 가능 <- BFS를 $S_i$만큼 수행

> [!tip] Time Complexity
> $O(N x M x P)$
