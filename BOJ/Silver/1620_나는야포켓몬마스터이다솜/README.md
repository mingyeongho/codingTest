### Algorithm: 자료구조, 해시를 사용한 집합과 맵

> [!abstract] 요구사항 분석
> 시간 제한: 2초
> 메모리 제한: 256MB

> [!question] 문제
> [문제 너무 김..](https://www.acmicpc.net/problem/1620)

> [!info] 입력
> 첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져. N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데, 자연수가 뭔지는 알지? 모르면 물어봐도 괜찮아. 나는 언제든지 질문에 답해줄 준비가 되어있어.
>
> 둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. 포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어. 아참! 일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야. 그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와. 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고, 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해. 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고, N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!

> [!success] 출력
> 첫째 줄부터 차례대로 M개의 줄에 각각의 문제에 대한 답을 말해줬으면 좋겠어!!!. 입력으로 숫자가 들어왔다면 그 숫자에 해당하는 포켓몬의 이름을, 문자가 들어왔으면 그 포켓몬의 이름에 해당하는 번호를 출력하면 돼. 그럼 땡큐~

> [!example] 예시1
> input
>
> ```
> 26 5
> Bulbasaur
> Ivysaur
> Venusaur
> Charmander
> Charmeleon
> Charizard
> Squirtle
> Wartortle
> Blastoise
> Caterpie
> Metapod
> Butterfree
> Weedle
> Kakuna
> Beedrill
> Pidgey
> Pidgeotto
> Pidgeot
> Rattata
> Raticate
> Spearow
> Fearow
> Ekans
> Arbok
> Pikachu
> Raichu
> 25
> Raichu
> 3
> Pidgey
> Kakuna
> ```
>
> output
>
> ```
> Pikachu
> 26
> Venusaur
> 16
> 14
> ```

> [!abstract] 내가 이해한 내용
> 포켓몬 도감에서
>
> 1. 포켓몬 이름이 입력되면 포켓몬 번호를 리턴
> 2. 포켓몬 번호가 입력되면 포켓몬 이름이 리턴

> [!tip] 문제의 본질 (어떠한 것을 나에게 물어보고 있는지)
> 입력이 100,000개이므로 입력마다 dict에 추가
> dict['pickchu'] = 1 이러면 1이 입력되었을 때 피카츄를 어떻게 알지

> [!hint] 아이디어
> dict에 포켓몬 이름이랑 번호를 같이 저장
> e.g. dex[pokemon] = i, dex[i] = pokemon

> [!success] 복잡도 분석
> 시간 복잡도:
> 공간 복잡도:

---

> [!info] 다른 사람의 풀이에서 알게된 것

---

[파이썬 웹 에디터](https://replit.com/@alsrudgh0210/KhakiPrettyClient#main.py)(커서를 사용하니까 다 알려줌;;)
