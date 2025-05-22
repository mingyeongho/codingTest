### Algorithm: 그래프 탐색

> [!abstract] 요구사항 분석
> 시간 제한: 3초
> 메모리 제한: 512MB

> [!question] 문제
> 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

> [!info] 입력
> 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

> [!success] 출력
> 첫째 줄에 연결 요소의 개수를 출력한다.

> [!example] 예시1
> input
>
> ```
> 6 5
> 1 2
> 2 5
> 5 1
> 3 4
> 4 6
> ```
>
> output
>
> ```
> 2
> ```

> [!example] 예시2
> input
>
> ```
> 6 8
> 1 2
> 2 5
> 5 1
> 3 4
> 4 6
> 5 4
> 2 4
> 2 3
> ```
>
> output
>
> ```
> 1
> ```

> [!abstract] 내가 이해한 내용
> 연결된 요소 뭉터기의 수를 구하여라

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 그래프 탐색을 사용한 구현

> [!hint] 아이디어
> BFS 사용
> while문을 사용해서 visited[1:]에 False가 있으면 수행
> startIndex는 visited[1:].index(False) + 1
> bfs 함수를 한번 수행하면 count 1 증가

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것

---

[파이썬 웹 에디터](https://replit.com/@alsrudgh0210/KhakiPrettyClient#main.py)(커서를 사용하니까 다 알려줌;;)
