### Algorithm: 그래프 탐색

> [!abstract] 요구사항 분석
> 시간 제한: 2초
> 메모리 제한: 128MB

> [!question] 문제
> 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2\*X의 위치로 이동하게 된다.
>
> 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

> [!info] 입력
> 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

> [!success] 출력
> 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

> [!example] 예시1
> input
>
> ```
> 5 17
> ```
>
> output
>
> ```
> 4
> ```

> [!abstract] 내가 이해한 내용
> X 위치에 있을 때 1초 후 갈 수 있는 위치는 $X-1,X+1,X\times2$ 이다.
> 풀이 방법은 모름

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)

> [!hint] 아이디어
> 찾아봄.
> bfs를 사용해서 풀이

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것

---

[파이썬 웹 에디터](https://replit.com/@alsrudgh0210/KhakiPrettyClient#main.py)(커서를 사용하니까 다 알려줌;;)
