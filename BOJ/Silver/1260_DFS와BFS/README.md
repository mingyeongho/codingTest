### Algorithm:

> [!abstract] 요구사항 분석
> 시간 제한: 2초
> 메모리 제한: 128MB

> [!question] 문제
> 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

> [!info] 입력
> 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

> [!success] 출력
> 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

> [!example] 예시1
> input
>
> ```
> 4 5 1
> 1 2
> 1 3
> 1 4
> 2 4
> 3 4
> ```
>
> output
>
> ```
> 1 2 4 3
> 1 2 3 4
> ```

> [!example] 예시2
> input
>
> ```
> 5 5 3
> 5 4
> 5 2
> 1 2
> 3 4
> 3 1
> ```
>
> output
>
> ```
> 3 1 2 5 4
> 3 1 4 2 5
> ```

> [!abstract] 내가 이해한 내용
> DFS와 BFS로 탐색한 노드의 순서를 출력

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> DFS와 BFS를 사용할 수 있냐

> [!hint] 아이디어
> 입력받은 노드들로 그래프 만들기
> DFS, BFS 함수 만들기

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것

---

[파이썬 웹 에디터](https://replit.com/@alsrudgh0210/KhakiPrettyClient#main.py)(커서를 사용하니까 다 알려줌;;)
