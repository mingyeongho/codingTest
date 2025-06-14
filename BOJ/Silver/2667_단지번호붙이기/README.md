### Algorithm: BFS, DFS

> [!abstract] 요구사항 분석
> 시간 제한: 1초
> 메모리 제한: 128MB

> [!question] 문제
> <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
>
> ![](https://www.acmicpc.net/upload/images/ITVH9w1Gf6eCRdThfkegBUSOKd.png)

> [!info] 입력
> 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

> [!success] 출력
> 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

> [!example] 예시1
> input
>
> ```
> 7
> 0110100
> 0110101
> 1110101
> 0000111
> 0100000
> 0111110
> 0111000
> ```
>
> output
>
> ```
> 3
> 7
> 8
> 9
> ```

> [!abstract] 내가 이해한 내용
> 연결된 1의 개수를 찾아라

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 이중 for 문을 돌며 bfs 진행

> [!hint] 아이디어
> 이중 for 문을 돌며 bfs를 진행
> bfs를 진행하며 1을 만나면 visited 처리

> [!success] 복잡도 분석
> 시간 복잡도: $O(N^2)$
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
