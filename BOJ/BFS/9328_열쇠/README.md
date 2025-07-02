Level: Gold1

> [!question] Question
> 훔칠 수 있는 문서의 최대 개수

> [!success] How?
> graph에 외곽 padding을 주어 (0, 0)에서 BFS 진입이 시작될 수 있도록 함
> 열지 않은 문에 대해 배열 안에 deque를 넣어서 관리 e.g. A를 열지 않았을 때 [deque([(0, 0)])] 이런 느낌

```python
elif re.match(r'[a-z]', cell):
	idx = ord(cell) - ord('a')
	if not keys[idx]:
		keys[idx] = True
		while door_wait[idx]:
			queue.append(door_wait[idx].popleft())
	queue.append((nx, ny))
elif re.match(r'[A-Z]', cell):
	idx = ord(cell.lower()) - ord('a')
	if keys[idx]:
		queue.append((nx, ny))
	else:
		door_wait[idx].append((nx, ny))
```

> [!info] Think
> 빌딩 가장자리에 들어갈 수 있는 좌표를 큐에 저장
> 큐에 popleft를 하면서 while문 수행
> 인접한 빈 공간에 이동할 수 있음.
> 문을 만나면 열쇠가 있는지 확인 후 열쇠가 있으면 큐에 추가
> 열쇠가 없으면 열지 못한 문큐에 좌표 추가
> 열쇠를 만나면 열쇠를 true로 하고 열지 못한 문들을 큐에 추가

> [!tip] Time Complexity
> $O(H x W)$
