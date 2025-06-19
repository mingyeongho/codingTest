Level: Platinum5

> [!question] Question
> N명이 한 줄로 서서 기다리고 있음.
> 두 사람 A와 B가 볼 수 있으려면 두 사람 사이에 A 또는 B보다 키가 큰 사람이 없어야 함.
> 서로 볼 수 있는 쌍의 수를 구하는 프로그램

> [!success] How?

> [!info] Think
> ⭐️ 이중 for문 부터 생각해보기
>
> ```python
> for i in range(n):
> 	for j in range(i+1, n):
> 		if heights[i] >= heights[j] :
> 			count += 1
> 		else:
> 			count +=1
> 			break # 나보다 큰 사람이 있으면 그 사람 뒤로는 나랑 눈이 마주칠 수 없음.
> ```
>
> ⭐️ 나보다 큰 사람이 있으면 그 사람 뒤로는 나랑 눈이 마주칠 수 없다를 유지하며 스택으로 바꾸기
> 흠.. 개어렵네

> [!tip] Time Complexity
> $O(N)$
