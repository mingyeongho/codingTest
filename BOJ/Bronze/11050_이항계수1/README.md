### Algorithm: 수학, 구현, 조합론

> [!abstract] 요구사항 분석
> 시간제한: 1초
> 메모리 제한: 256MB
>
> | 입력 크기 N (대략) | 1 초에 통과 가능한 권장 시간 복잡도   |
> | ------------------ | ------------------------------------- |
> | **N ≤ 500**        | `O(N³)` 까지도 가능 (삼중 루프)       |
> | **N ≤ 2 000**      | `O(N²)` 정도까지 (이중 루프)          |
> | **N ≤ 100,000**    | `O(N log N)` 필요 (정렬, 트리/힙 등)  |
> | **N ≤ 10,000,000** | `O(N)` 또는 더 빠른 알고리즘/자료구조 |

> [!question] 문제
> 자연수 N과 정수 K가 주어졌을 때 이항 계수 $\binom{N}{K}$를 구하는 프로그램을 작성하시오.

> [!info] 입력
> 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 0 ≤ K ≤ N)

> [!success] 출력
> $\binom{N}{K}$ 를 출력한다.

> [!abstract] 내가 이해한 내용
> N과 K가 주어졌을 때 이항 계수 $\binom{N}{K}$를 구하여라

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 이항 계수를 구하는 방법을 알고 있는가
> $\binom{N}{K}=N!/(K!\times(N-K)!)$

> [!hint] 아이디어
> 팩토리얼을 구하는 함수를 만듦

---

> [!example] 예시1
> input
>
> ```
> 5 2
> ```
>
> output
>
> ```
> 10
> ```

> [!example] 예시2
> input
>
> ```
> 4 3
> ```
>
> output
>
> ```
> 4
> ```

---

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
> import math
> math.factorial $O(N)$

---

[파이썬 웹 에디터](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)(커서를 사용하니까 다 알려줌;;)
