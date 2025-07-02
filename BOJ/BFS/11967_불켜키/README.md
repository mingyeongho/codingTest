Level: Gold2

> [!question] Question
> 최대한 많은 방에 불을 밝히고 싶다.
> 어떤 방에는 다른 방의 불을 끄고 켤 수 있는 스위치가 달려있다
> 베시는 불이 켜져있는 방으로만 들어갈 수 있다.
> 베시가 불을 켤 수 있는 방의 최대 개수를 구하는 프로그램

> [!success] How?
> bright 2d array와 visited 2d array를 만듦.
> (0, 0)은 불이 켜져있고 방문도 한 상태
> 큐를 돌면서 현재 방에서 킬 수 있는 불을 다 킴
> 불을 킨 방을 현재 내가 갈 수 있으면 큐에 추가하고 visited도 추가
> 현재 내가 갈 수 있는 방도 큐에 추가하고 visited도 추가

> [!info] Think

> [!tip] Time Complexity
