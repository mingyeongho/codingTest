### Algorithm: 백트래킹

> [!abstract] 요구사항 분석
> 시간 제한: 1초
> 메모리 제한: 512MB

> [!question] 문제
> 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
>
> - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
> - 고른 수열은 오름차순이어야 한다.

> [!info] 입력
> 첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

> [!success] 출력
> 한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
>
> 수열은 사전 순으로 증가하는 순서로 출력해야 한다.

> [!example] 예시1
> input
>
> ```
> 3 1
> ```
>
> output
>
> ```
> 1
> 2
> 3
> ```

> [!abstract] 내가 이해한 내용
> N과M(1)이랑 똑같은데 '고른 수열은 오름차순이어야 한다.' 이것만 생각하면 됨.

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> isUsed를 할 때 현재 i값보다 작은 애들은 다 isUsed = True로

> [!hint] 아이디어
> isUsed를 할 때 현재 i값보다 작은 애들은 다 isUsed = True로

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
