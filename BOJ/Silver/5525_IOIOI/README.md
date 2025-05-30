### Algorithm: 문자열

> [!abstract] 요구사항 분석
> 시간 제한: 1초
> 메모리 제한: 256MB
> 1 ≤ N ≤ 1,000,000
> 2N+1 ≤ M ≤ 1,000,000

> [!question] 문제
> N+1개의 `I`와 N개의 `O`로 이루어져 있으면, `I`와 `O`이 교대로 나오는 문자열을 PN이라고 한다.
>
> - P1 `IOI`
> - P2 `IOIOI`
> - P3 `IOIOIOI`
> - PN `IOIOI...OI` (`O`가 N개)
>
> `I`와 `O`로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램을 작성하시오.

> [!info] 입력
> 첫째 줄에 N이 주어진다. 둘째 줄에는 S의 길이 M이 주어지며, 셋째 줄에 S가 주어진다.

> [!success] 출력
> S에 $Pn$이 몇 군데 포함되어 있는지 출력한다.

> [!example] 예시1
> input
>
> ```
> 1
> 13
> OOIOIOIOIIOII
> ```
>
> output
>
> ```
> 4
> ```

> [!abstract] 내가 이해한 내용
> $Pn$은 n+1개의 I와 n개의 O이 교대로 나오는 문자열
> n이 주어질 때 문자열 S안에 $Pn$이 몇 개 있는지 구하는 문제

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 시간 제한을 맞춰서 코드 구현
> IOI의 반복

> [!hint] 아이디어
> IOI의 반복으로 구현

> [!success] 복잡도 분석
> 시간 복잡도: $O(N)$
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것

---

[파이썬 웹 에디터](https://replit.com/@alsrudgh0210/KhakiPrettyClient#main.py)(커서를 사용하니까 다 알려줌;;)
