Level: Silver3

> [!question] Question
> 자연수 N과 M이 주어질 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
>
> - 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

> [!success] How?
> 특정 수가 사용되었는지를 확인하는 배열 is_used를 만듦.
> is_used는 bool 값을 가지는 N+1 길이의 배열
> 수열을 저장하는 ans 배열을 만듦.
> ans 배열은 0을 기본으로 가지는 M 길이의 배열
> backtrack 함수를 재귀적으로 호출하여 해결
> backtrack은 k번째 인덱스에 값을 채우는 함수
> base condition
>
> - k가 M과 같으면 ans 수열을 출력
>
> for 문을 돌며 is_used[i]가 False이면 ans에 추가하고 is_used 값 바꾸고 backtrack k+1 호출

> [!info] Think

> [!tip] Time Complexity
