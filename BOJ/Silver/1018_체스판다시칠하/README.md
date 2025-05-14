### Algorithm: 구현, 브루트포스

> [!abstract] 요구사항 분석
> 시간제한: 2초
> 메모리 제한: 128MB
> $8 \leq N, M \leq 50$

> [!question] 문제
> 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다. 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다. 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
>
> 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다. 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
>
> 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다. 당연히 8\*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.

> [!info] 입력
> 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.

> [!success] 출력
> 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

> [!example] 예시1
> input
>
> ```
> 8 8
> WBWBWBWB
> BWBWBWBW
> WBWBWBWB
> BWBBBWBW
> WBWBWBWB
> BWBWBWBW
> WBWBWBWB
> BWBWBWBW
> ```
>
> output
>
> ```
> 1
> ```

> [!example] 예시2
> input
>
> ```
> 10 13
> BBBBBBBBWBWBW
> BBBBBBBBBWBWB
> BBBBBBBBWBWBW
> BBBBBBBBBWBWB
> BBBBBBBBWBWBW
> BBBBBBBBBWBWB
> BBBBBBBBWBWBW
> BBBBBBBBBWBWB
> WWWWWWWWWWBWB
> WWWWWWWWWWBWB
> ```
>
> output
>
> ```
> 12
> ```

> [!abstract] 내가 이해한 내용
> $M \times N$ 보드를 $8 \times 8$로 잘라서 체스판을 만듦.
> 검은색과 흰색이 번갈아가며 칠해져있어야 한다.
> 맨 왼쪽 위칸이 검은색 or 흰색
> 다시 칠해야 하는 정사각형의 최소 개수

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)

> [!hint] 아이디어
>
> 1. $M \times N$이 주어졌을 때 얘로 만들 수 있는 $8 \times 8$의 체스판을 모두 만들어보고
> 2. 각 체스판마다 몇 개의 정사각형을 바꿔야 하는지 계산

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
> 개어려운디;;;;;
> [문제풀이 동영상](https://www.youtube.com/watch?v=98TMUoYCCEE) > [문제풀이 코드](https://roamingman.tistory.com/6)

---

[파이썬 웹 에디터](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)(커서를 사용하니까 다 알려줌;;)
