Level: Silver2

> [!question] Question
> N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분 수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램

> [!success] How?
> 백트래킹을 사용해서 모든 후보군을 확인해야함.
>
> 1. base condition
>    - 총합 == S와 같으면 count 증가
>    - len이 N과 같으면 끝
> 2. 재귀식
>    - is_used 사용, 본인 미포함
>    - start 사용, 중복되는 부분 수열이 없어야 함.

> [!info] Think

> [!tip] Time Complexity
