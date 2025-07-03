Level: Silver1

> [!question] Question
> 자연수 A를 B번 곱한 수를 알고 싶다.
> 구하려는 수가 매우 커질 수 있으므로 이를 C로 나눈 나머지를 구하는 프로그램

> [!success] How?
> e.g. 10 11 12
> 10을 11번 곱한 수를 12로 나눈 값

> [!info] Think
> $A^B = A^{B/2} \times A^{B/2}$ if B is even
> $A^B = A \times A^{B-1}$ if B is odd

> [!tip] Time Complexity
> $O(logB)$
