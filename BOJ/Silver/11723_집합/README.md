### Algorithm: 구현, 비트마스킹

> [!abstract] 요구사항 분석
> 시간 제한: 1.5초
> 메모리 제한: 4MB

> [!question] 문제
> 비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
>
> - `add x`: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
> - `remove x`: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
> - `check x`: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
> - `toggle x`: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
> - `all`: S를 {1, 2, ..., 20} 으로 바꾼다.
> - `empty`: S를 공집합으로 바꾼다.

> [!info] 입력
> 첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
>
> 둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

> [!success] 출력
> `check` 연산이 주어질때마다, 결과를 출력한다.

> [!example] 예시1
> input
>
> ```
> 26
> add 1
> add 2
> check 1
> check 2
> check 3
> remove 2
> check 1
> check 2
> toggle 3
> check 1
> check 2
> check 3
> check 4
> all
> check 10
> check 20
> toggle 10
> remove 20
> check 10
> check 20
> empty
> check 1
> toggle 1
> check 1
> toggle 1
> check 1
> ```
>
> output
>
> ```
> 1
> 1
> 0
> 1
> 0
> 1
> 0
> 1
> 0
> 1
> 1
> 0
> 0
> 0
> 1
> 0
> ```

> [!abstract] 내가 이해한 내용

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 비트 마스킹을 사용해 구현해보기

> [!hint] 아이디어
> add n
>
> - s |= (1 << n)
>   remove n
> - s &= ~(1 << n)
>   toggle n
> - s ^= (1 << n)
>   check
> - s & (1 << n)

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것

---

[파이썬 웹 에디터](https://replit.com/@alsrudgh0210/KhakiPrettyClient#main.py)(커서를 사용하니까 다 알려줌;;)
