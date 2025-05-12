### Algorithm: 수학

> [!abstract] 요구사항 분석
> 시간제한: 2초
> 메모리 제한: 128MB
> 0 ≤ N ≤ 500

> [!question] 문제
> N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

> [!info] 입력
> 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

> [!success] 출력
> 첫째 줄에 구한 0의 개수를 출력한다.

> [!abstract] 내가 이해한 내용
> N!을 한 값의 뒤에서 0이 연속해서 몇 개 나오느냐

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)

> [!hint] 아이디어
> factorial을 하고 뒤에서부터 0의 갯수 세기

---

> [!example] 예시1
> input
>
> ```
> 10
> ```
>
> output
>
> ```
> # 10! = 3628800
> 2
> ```

> [!example] 예시2
> input
>
> ```
> 3
> ```
>
> output
>
> ```
> # 3! = 6
> 0
> ```

---

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
>
> ```
> n = int(input())
> print(n//5 + n//25 + n//125)
> ```
>
> 이게 뭐고..
> 0이 늘어나는 순간은 10이 곱해졌을 때이다.
>
> > [!example] 예시
> > $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$ > > $10! = 10 \times 9 \times 8 \times ... \times 2 \times 1 = 3628800$
> > 5의 배수가 나올 때 0이 하나씩 늘어난다.
> > 5!은 5가 1개 나옴
> > 10!은 5개 2개 나옴 (5, $10=2\times5$)
>
> 5의 배수의 개수는 5로 나눈 몫이다.
> 25 같은 값은 5개 2개 들어간다.

---

[파이썬 웹 에디터](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)(커서를 사용하니까 다 알려줌;;)
