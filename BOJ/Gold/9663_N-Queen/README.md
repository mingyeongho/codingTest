### Algorithm: 백트래킹

> [!abstract] 요구사항 분석
> 시간 제한: 10초
> 메모리 제한: 128MB

> [!question] 문제
> N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
>
> N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

> [!info] 입력
> 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

> [!success] 출력
> 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

> [!example] 예시1
> input
>
> ```
> 8
> ```
>
> output
>
> ```
> 92
> ```

> [!abstract] 내가 이해한 내용
> n x n의 체스칸이 주어질 때 놓을 수 있는 퀸의 개수

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 퀸을 놓을 수 없는 자리를 어떻게 알 것인가

> [!hint] 아이디어
> isUsed 배열을 세 개 만들어서 사용
> isUsedCol - j
> isUsedLCross - k + j
> isUsedRCross - k - j + n - 1 <- 요게 생각하기가 어려움
> isUsed 배열만 만들면 백트래킹 슥삭 가능

> [!success] 복잡도 분석
> 시간 복잡도: $O(N!)$
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
