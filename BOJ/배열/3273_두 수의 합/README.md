Level: Sliver3

> [!question] Question
> 서로 다른 양의 정수 리스트와 타겟 값이 주어질 때 a + b = x를 만족하는 (a, b) 쌍의 수를 구하는 프로그램

> [!success] How?
> 길이가 1_000_001인 boolean을 값으로 가지는 배열을 만든다. (default: False)
> 입력받은 수열을 순회하며 인덱스의 값을 True로 바꾼다.
> x-a의 값이 True이면 count를 증가시킨다.

> [!info] Think
> 이중 for문은 시간 제한 때문에 사용할 수 없다.
> O(N) 시간 복잡도로 해결할 수 있어야 함.

> [!tip] 시간 복잡도
> $O(N)$
