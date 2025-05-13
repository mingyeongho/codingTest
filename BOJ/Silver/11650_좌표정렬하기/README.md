### Algorithm: 정렬

> [!abstract] 요구사항 분석
> 시간 제한: 1초
> 메모리 제한: 256MB
> N ≤ 100,000

> [!question] 문제
> 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

> [!info] 입력
> 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

> [!success] 출력
> 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

> [!example] 예시1
> input
>
> ```
> 5
> 3 4
> 1 1
> 1 -1
> 2 2
> 3 3
> ```
>
> output
>
> ```
> 1 -1
> 1 1
> 2 2
> 3 3
> 3 4
> ```

> [!abstract] 내가 이해한 내용
> 정렬 알고리즘
> 1초 + N = 100,000 개 => $O(NlogN)$

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> sort 사용

> [!hint] 아이디어
> 입력한 값을 다 map을 사용해서 int로 변환하고 sorted + key에 x좌표 먼저 y좌표 나중으로 설정

> [!success] 복잡도 분석
> 시간 복잡도: $O(NlogN)$
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것

---

[파이썬 웹 에디터](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)(커서를 사용하니까 다 알려줌;;)
