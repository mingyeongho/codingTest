### Algorithm: 문자열, 정렬

> [!abstract] 요구사항 분석
> 시간제한: 2초
> 메모리 제한: 256MB
> 단어의 개수: $1 \leq N \leq 20,000$
> 문자열의 길이: $1 \leq L \leq 50$

> [!question] 문제
> 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
>
> 1. 길이가 짧은 것부터
> 2. 길이가 같으면 사전 순으로
>
> 단, 중복된 단어는 하나만 남기고 제거해야 한다.

> [!info] 입력
> 첫째 줄에 단어의 개수 N이 주어진다. (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 주어지는 문자열의 길이는 50을 넘지 않는다.

> [!success] 출력
> 조건에 따라 정렬하여 단어들을 출력한다.

> [!abstract] 내가 이해한 내용
> 입력받은 단어들 중 중복된 단어는 하나만 남기고 제거.
> 문자열의 길이가 짧은 순서대로 정렬
> 문자열의 길이가 같다면 사전순으로 정렬

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 구현

> [!hint] 아이디어
> 중복 제거: set() or for ... if a in data
> 문자열 길이가 짧은 순으로 정렬: 계수 정렬 비슷하게?

---

> [!example] 예시1
> input
>
> ```
> 13
> but
> i
> wont
> hesitate
> no
> more
> no
> more
> it
> cannot
> wait
> im
> yours
> ```
>
> output
>
> ```
> i
> im
> it
> no
> but
> more
> wait
> wont
> yours
> cannot
> hesitate
> ```

---

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
> 중복제거는 set()을 하는게 훨씬 빠름

---

[파이썬 웹 에디터](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)(커서를 사용하니까 다 알려줌;;)
