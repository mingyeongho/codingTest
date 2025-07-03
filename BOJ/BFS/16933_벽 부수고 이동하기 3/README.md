Level: Gold1

> [!question] Question
> 벽을 K개 부수고 이동 가능
> 낮과 밤이 번갈아가며 등장, 이동하지 않고 머무르는 경우도 존재
> 벽은 낮에만 부술 수 있다.

> [!success] How?
> 밤에는 거리만 1추가하고 큐에 넣기
> ⭐️ visited 3d array에 거리도 같이 저장하고 이 거리로 낮인지 밤인지 판별

> [!info] Think
> 하루 더 머무를 때 큐에 dist+2가 된 좌표를 바로 넣으면 안됨.

> [!tip] Time Complexity
