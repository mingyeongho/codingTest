Level: Gold3

> [!question] Question
> 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다.
> 자기 자신을 선택하는 것도 가능
> 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산

> [!success] How?

> [!info] Think
>
> ```python
> def dfs(x):
> 	global count
> 	visited[x] = True
> 	team.append(x)
> 	nxt = choice[x]
> 	if not visited[nxt]:
> 	    dfs(nxt)
> 	else:
> 	    if nxt in team:
> 			count += len(team[team.index(nxt):])
> ```

> [!tip] Time Complexity
