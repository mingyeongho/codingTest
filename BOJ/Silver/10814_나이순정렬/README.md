### Algorithm: 정렬

> [!abstract] 요구사항 분석
> 시간 제한: 3초
> 메모리 제한: 256MB
> $N \leq 100,000$

> [!question] 문제
> 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

> [!info] 입력
> 첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)
>
> 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

> [!success] 출력
> 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

> [!example] 예시1
> input
>
> ```
> 3
> 21 Junkyu
> 21 Dohyun
> 20 Sunyoung
> ```
>
> output
>
> ```
> 20 Sunyoung
> 21 Junkyu
> 21 Dohyun
> ```

> [!example] 예시2
> input
>
> ```
>
> ```
>
> output
>
> ```
>
> ```

> [!abstract] 내가 이해한 내용
> 입력한 회원을 나이 순으로 출력해라.

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 어떤 알고리즘을 사용할 것이냐
> N의 범위나 시간 제한이 넉넉한 거 같아서 sorted 사용하면 될 듯

> [!hint] 아이디어
> 각 입력을 [(나이, 이름), (나이, 이름), ...] 이런 식으로 저장하고 sorted와 key를 사용해서 나이순으로 정렬

> [!success] 복잡도 분석
> 시간 복잡도: $O(NlogN)$
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
> `members = [(int(age), name) for age, name in (input().split() for _ in range(n))]`
> 리스트 컴프리헨션을 사용해서 입력과 동시에 값을 int로 변환하여 저장

---

[파이썬 웹 에디터](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)(커서를 사용하니까 다 알려줌;;)
