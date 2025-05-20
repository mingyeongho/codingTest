### Algorithm: 다이나믹 프로그래밍

> [!abstract] 요구사항 분석
> 시간 제한: 1초
> 메모리 제한: 256MB

> [!question] 문제
> 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
>
> 아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.
>
> ![](https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/11726/1.png)

> [!info] 입력
> 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

> [!success] 출력
> 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

> [!example] 예시1
> input
>
> ```
> 2
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
> 9
> ```
>
> output
>
> ```
> 55
> ```

> [!abstract] 내가 이해한 내용

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 다이나믹 프로그래밍으로 문제 해결

> [!hint] 아이디어
> i >= 3
> dp[i] = dp[i-1] + dp[i-2]

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것

---

[파이썬 웹 에디터](https://replit.com/@alsrudgh0210/KhakiPrettyClient#main.py)(커서를 사용하니까 다 알려줌;;)
