Level: Gold4

> [!question] Question
> 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
> 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽에 있는 수

> [!success] How?
> e.g. [3, 5, 2, 7] -> 5 7 7 -1
> res 배열을 -1로 초기화
> 얘도 스택에 튜플로 인덱스와 값을 저장해야함.
> 기존 수열에 pop 수행 7, stk가 비어있으니 stk.append((idx, 7))
> 수열에 pop 수행 2, stk의 마지막 원소의 값이 7이라서 2보다 크니까 res[idx] = 7
> 수열에 pop 수행 5, stk의 마지막 원소의 값이 2

> [!info] Think
> pop을 쓰는 방법이 있고 stk의 idx를 쓰는 방법이 있음

> [!tip] Time Complexity
> $O(N)$
