Level: Silver2

> [!question] Question
> 자연수 중 같은 수를 가진 수가 있다.
> 중복되는 수열을 여러 번 출력하면 안된다.

> [!success] How?
> set 사용

> [!info] Think
> sorted는 문자열 기준 정렬
> 숫지 기준 정렬이 필요함.
> `sorted(res, key=lamnbda x: list(map(int, x.split())))`

> [!tip] Time Complexity
