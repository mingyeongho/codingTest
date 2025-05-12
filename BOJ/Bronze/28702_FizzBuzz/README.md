### Algorithm: 수학, 문자열

> [!abstract] 요구사항 분석
> 시간제한: 0.5초
> 메모리 제한: 1024MB

> [!question] 문제
> FizzBuzz 문제는 i=1,2,⋯$i = 1, 2, \cdots$ 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.
>
> - $i$가 $3$의 배수이면서 $5$의 배수이면 “`FizzBuzz`”를 출력합니다.
> - $i$가 $3$의 배수이지만 $5$의 배수가 아니면 “`Fizz`”를 출력합니다.
> - $i$가 $3$의 배수가 아니지만 $5$의 배수이면 “`Buzz`”를 출력합니다.
> - $i$가 $3$의 배수도 아니고 $5$의 배수도 아닌 경우 $i$를 그대로 출력합니다.
>
> FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?

> [!info] 입력
> FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 한 줄에 하나씩 주어집니다. 각 문자열의 길이는 $8$ 이하입니다. 입력이 항상 FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열에 대응됨이 보장됩니다.

> [!success] 출력
> 연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력하세요. 여러 문자열이 올 수 있는 경우, 아무거나 하나 출력하세요.

> [!abstract] 내가 이해한 내용
> 세 번의 입력 후 다음에 올 값을 출력해라
> 입력된 값은 i, Fizz, Buzz, FizzBuzz가 될 수 있다.
> Fizz, Buzz, FizzBuzz는 조건이 있고 i는 자연수이다.

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 구현

> [!hint] 아이디어
> 입력된 세 개의 값들 중 하나라도 숫자면 출력될 값을 알 수 있다.
> 첫번째 값이 숫자: value + 3
> 두번째 값이 숫자: value + 2
> 세번째 값이 숫자: value + 1
> 모든 수가 숫자가 아닐 경우: 아무거나 하나 출력? <- 케이스 확인 필요

---

> [!example] 예시1
> input
>
> ```
> Fizz
> Buzz
> 11
> ```
>
> output
>
> ```
> Fizz
> ```

> [!example] 예시2
> input
>
> ```
> 980803
> 980804
> FizzBuzz
> ```
>
> output
>
> ```
> 980806
> ```

> [!example] 예시3
> input
>
> ```
> Fizz
> 4
> Buzz
> ```
>
> output
>
> ```
> Fizz
> ```

---

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것
> isdecimal: int() 할 수 있는 것만 True
> isdigit: 거듭제곱 형태도 True
> isnumeric: 거듭제곱, 분수, 제곱근도 True

---

[파이썬 웹 에디터](https://www.onlineide.pro/playground/python?utm_source=online-python&utm_medium=navbar&utm_campaign=onlineidepro)(커서를 사용하니까 다 알려줌;;)
