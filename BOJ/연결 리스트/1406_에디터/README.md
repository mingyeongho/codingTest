Level: Silver2

> [!question] Question
> 한 줄로 된 간단한 에디터를 구현
> 시간 제한: 0.3초
> L: 커서를 왼쪽으로 한 칸 옮김
> D: 커서를 오른쪽으로 한 칸 옮김
> B: 커서 왼쪽에 있는 문자열 삭제
> P $: $라는 문자를 왼쪽에 추가함

> [!success] How?
> 커서를 기준으로 왼쪽에 있는 문자열과 오른쪽에 있는 문자열 스택을 만들어서 append와 pop을 수행하며 명령어 구현.
> O(1) 시간 복잡도를 가지므로 시간 제한 내 수행 가능

> [!info] Think
> pop할 때 head와 tail이 존재하는지 확인해야함.
> sep를 쓰는것보다 join을 쓰는게 더 빠름 + 메모리도 더 적게듬

> [!tip] 시간 복잡도
> $O(M+N)$
