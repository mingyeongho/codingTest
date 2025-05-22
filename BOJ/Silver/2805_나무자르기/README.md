### Algorithm: 이진 탐색, 매개변수 탐색

> [!abstract] 요구사항 분석
> 시간 제한: 1초
> 메모리 제한: 256MB

> [!question] 문제
> 상근이는 나무 M미터가 필요하다. 근처에 나무를 구입할 곳이 모두 망해버렸기 때문에, 정부에 벌목 허가를 요청했다. 정부는 상근이네 집 근처의 나무 한 줄에 대한 벌목 허가를 내주었고, 상근이는 새로 구입한 목재절단기를 이용해서 나무를 구할것이다.
>
> 목재절단기는 다음과 같이 동작한다. 먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 낮은 나무는 잘리지 않을 것이다. 예를 들어, 한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 상근이가 높이를 15로 지정했다면, 나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. (총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.
>
> 상근이는 환경에 매우 관심이 많기 때문에, 나무를 필요한 만큼만 집으로 가져가려고 한다. 이때, 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

> [!info] 입력
> 첫째 줄에 나무의 수 N과 상근이가 집으로 가져가려고 하는 나무의 길이 M이 주어진다. (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
>
> 둘째 줄에는 나무의 높이가 주어진다. 나무의 높이의 합은 항상 M보다 크거나 같기 때문에, 상근이는 집에 필요한 나무를 항상 가져갈 수 있다. 높이는 1,000,000,000보다 작거나 같은 양의 정수 또는 0이다.

> [!success] 출력
> 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력한다.

> [!example] 예시1
> input
>
> ```
> 4 7
> 20 15 10 17
> ```
>
> output
>
> ```
> 15
> ```

> [!example] 예시2
> input
>
> ```
> 5 20
> 4 42 40 26 46
> ```
>
> output
>
> ```
> 36
> ```

> [!abstract] 내가 이해한 내용
> 나무들의 높이가 주어질 때 적어도 m을 만들 수 있는 톱날 높이의 최댓값

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 이진 탐색을 사용한 구현

> [!hint] 아이디어

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
> `total = sum([height - mid for height in heights if height >= mid])`
> 위 코드에서 if문 쪽을 안써줘서 실패함.

```python
# Time: 460ms
import sys
input = sys.stdin.readline

from collections import Counter

N, M = map(int, input().split())
trees = list(map(int, input().split()))

counted = Counter(trees)


bottom = 0
top = 1000000000

res = 0

while bottom <= top:
    middle = (bottom + top)//2

    # middle 체크
    tmp = 0
    # for h in trees:
    #     if h >= middle:
    #         tmp += h-middle
    for height, cnt in counted.items():
        if height >= middle:
            tmp += (height-middle) * cnt

    if tmp >= M:
        res = max(res, middle)
        bottom = middle + 1
    else:
        top = middle - 1

print(res)
```

Counter로 중복되는 수는 합쳐서 계산

---

[파이썬 웹 에디터](https://replit.com/@alsrudgh0210/KhakiPrettyClient#main.py)(커서를 사용하니까 다 알려줌;;)
