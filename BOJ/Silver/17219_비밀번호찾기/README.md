### Algorithm: 자료구조, 해시를 사용한 집합과 맵

> [!abstract] 요구사항 분석
> 시간 제한: 5초
> 메모리 제한: 256MB

> [!question] 문제
> 2019 HEPC - MAVEN League의 "[비밀번호 만들기](https://www.acmicpc.net/problem/17218)"와 같은 방식으로 비밀번호를 만든 경민이는 한 가지 문제점을 발견하였다. 비밀번호가 랜덤으로 만들어져서 기억을 못 한다는 것이었다! 그래서 경민이는 메모장에 사이트의 주소와 비밀번호를 저장해두기로 했다. 하지만 컴맹인 경민이는 메모장에서 찾기 기능을 활용하지 못하고 직접 눈으로 사이트의 주소와 비밀번호를 찾았다. 메모장에 저장된 사이트의 수가 늘어나면서 경민이는 비밀번호를 찾는 일에 시간을 너무 많이 쓰게 되었다. 이를 딱하게 여긴 문석이는 경민이를 위해 메모장에서 비밀번호를 찾는 프로그램을 만들기로 결심하였다! 문석이를 도와 경민이의 메모장에서 비밀번호를 찾아주는 프로그램을 만들어보자.

> [!info] 입력
> 첫째 줄에 저장된 사이트 주소의 수 N(1 ≤ N ≤ 100,000)과 비밀번호를 찾으려는 사이트 주소의 수 M(1 ≤ M ≤ 100,000)이 주어진다.
>
> 두번째 줄부터 N개의 줄에 걸쳐 각 줄에 사이트 주소와 비밀번호가 공백으로 구분되어 주어진다. 사이트 주소는 알파벳 소문자, 알파벳 대문자, 대시('-'), 마침표('.')로 이루어져 있고, 중복되지 않는다. 비밀번호는 알파벳 대문자로만 이루어져 있다. 모두 길이는 최대 20자이다.
>
> N+2번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소가 한줄에 하나씩 입력된다. 이때, 반드시 이미 저장된 사이트 주소가 입력된다.

> [!success] 출력
> 첫 번째 줄부터 M개의 줄에 걸쳐 비밀번호를 찾으려는 사이트 주소의 비밀번호를 차례대로 각 줄에 하나씩 출력한다.

> [!example] 예시1
> input
>
> ```
> 16 4
> noj.am IU
> acmicpc.net UAENA
> startlink.io THEKINGOD
> google.com ZEZE
> nate.com VOICEMAIL
> naver.com REDQUEEN
> daum.net MODERNTIMES
> utube.com BLACKOUT
> zum.com LASTFANTASY
> dreamwiz.com RAINDROP
> hanyang.ac.kr SOMEDAY
> dhlottery.co.kr BOO
> duksoo.hs.kr HAVANA
> hanyang-u.ms.kr OBLIVIATE
> yd.es.kr LOVEATTACK
> mcc.hanyang.ac.kr ADREAMER
> startlink.io
> acmicpc.net
> noj.am
> mcc.hanyang.ac.kr
> ```
>
> output
>
> ```
> THEKINGOD
> UAENA
> IU
> ADREAMER
> ```

> [!abstract] 내가 이해한 내용
> 주소와 비밀번호를 dict에 넣고
> 주소가 입력되면 비밀번호를 출력

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> dict

> [!hint] 아이디어

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것

---

[파이썬 웹 에디터](https://replit.com/@alsrudgh0210/KhakiPrettyClient#main.py)(커서를 사용하니까 다 알려줌;;)
