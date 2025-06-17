Level: Bronze2

> [!question] Question
> $a \times b \times c$를 계산한 결과에 0부터 9까지의 숫자가 몇 번 쓰였는지 구하는 프로그램

> [!success] How?
> $a \times b \times c$를 문자로 변환한 후 순회한다.
> 0부터 9까지 숫자 카운트를 담는 배열을 만든다.
> 계산한 결과를 순회하며 카운트 배열의 각 인덱스의 값을 증가시킨다.
> 순회하는 문자와 인덱스가 같기 때문에 int(c)를 사용하면 됨.

> [!info] Think

> [!tip] 시간 복잡도
> $O(D) D는 a*b*c$
