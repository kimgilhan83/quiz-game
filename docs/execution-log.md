# 실행 로그 (터미널 출력 발췌)

모든 내용은 실제 터미널에서 실행한 결과를 그대로 옮긴 것입니다. (이메일은 마스킹)

## 1. 개발 환경

```
$ python3 --version
Python 3.14.4
$ git --version
git version 2.53.0
$ git config --list
user.name=kimgilhan83
user.email=*****@gmail.com
init.defaultbranch=main
```

## 2. 퀴즈 추가

```
선택: 2

📌 새로운 퀴즈를 추가합니다.
문제를 입력하세요: 할인이란
선택지 1: 이야
선택지 2: 우와
선택지 3: 대박
선택지 4: 상술
정답 번호 (1-4): 1
✅ 퀴즈가 추가되었습니다!
```

## 3. 퀴즈 목록

```
선택: 3

📋 등록된 퀴즈 목록 (총 6개)
----------------------------------------
[1] 물가가 지속적으로 오르는 현상을 무엇이라고 할까요?
[2] 중앙은행이 물가를 잡기 위해 조정하는 대표적인 수단은?
[3] 1달러가 1,300원에서 1,400원으로 올랐습니다. 원화의 가치는?
[4] '계란을 한 바구니에 담지 말라'는 투자 격언이 뜻하는 것은?
[5] 원금뿐 아니라 이미 붙은 이자에도 이자가 붙는 방식은?
[6] 할인이란
----------------------------------------
```

## 4. 퀴즈 풀기와 점수 확인

```
========================================
🏆 결과: 5문제 중 2문제 정답! (40점)
========================================
🎉 새로운 최고 점수입니다!
...
선택: 4
🏆 최고 점수: 40점
```

점수가 없을 때:

```
선택: 4
⚠️ 아직 퀴즈를 풀지 않았습니다.
```

## 5. 종료 후 재실행 시 데이터 유지

```
$ python3 main.py
📂 저장된 데이터를 불러왔습니다. (퀴즈 6개, 최고점수 33점)
```

## 6. 예외 처리

저장 파일 손상:

```
$ echo "{ 깨진 내용" > state.json
$ python3 main.py
⚠️ 저장 파일이 손상되어 기본 퀴즈로 초기화합니다.
```

저장 파일 없음 후 Ctrl+C:

```
$ rm state.json
$ python3 main.py
📂 저장된 데이터가 없어 기본 퀴즈로 시작합니다.
선택:
입력이 중단되었습니다. 안전하게 종료합니다.
```

## 7. clone과 pull

```
$ git clone https://github.com/kimgilhan83/quiz-game.git quiz-game-clone
Cloning into 'quiz-game-clone'...
Receiving objects: 100% (61/61), 14.89 KiB | 1.65 MiB/s, done.
$ cd quiz-game-clone
$ ls -a
.  ..  .git  .gitignore  README.md  main.py
```

복제본에서 수정 후 push:

```
$ git commit -m "Docs: clone/pull 실습용 README 한 줄 추가"
[main fa46e49] Docs: clone/pull 실습용 README 한 줄 추가
$ git push
   ecb5b8b..fa46e49  main -> main
```

원본 폴더에서 pull:

```
$ cd ~/quiz-game
$ git pull
From https://github.com/kimgilhan83/quiz-game
   ecb5b8b..fa46e49  main       -> origin/main
Updating ecb5b8b..fa46e49
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
```

## 8. Git 이력 그래프

* fa46e49 (HEAD -> main, origin/main, origin/HEAD) Docs: clone/pull 실습용 README 한 줄 추가
* ecb5b8b Docs: README 작성
* 43ffc75 Fix: readline이 없는 환경(윈도우)에서도 실행되도록 수정
* c490bbb Chore: state.json을 .gitignore에 추가
* 3f7be91 Feat: state.json 저장 및 불러오기 구현
* d9e0bf8 Fix: 임시 테스트 코드 제거
* a4fb7a7 Feat: Quiz 저장용 변환 메서드 추가
* ca7099a Refactor: 퀴즈 목록을 QuizGame 메서드로 이동
* 6777e06 Refactor: QuizGame 클래스 도입
* 197ebf3 Feat: 최고 점수 확인 및 갱신 기능 구현
* 7c3392e Fix: 한글 입력 시 백스페이스로 글자가 깨지는 문제 수정
* 3f51d63 Feat: 퀴즈 추가 기능 구현
* 3e5b913 Feat: 퀴즈 목록 기능 구현
*   ae49c01 Merge: 퀴즈 풀기 기능 병합
|\
| * 52050ae (origin/feature/quiz-play, feature/quiz-play) Feat: 퀴즈 풀기 기능 구현
| * 263db27 Feat: 숫자 입력 검증 함수 추가
|/
* d2970d0 Feat: 경제 기본 퀴즈 5개 작성
* 24792f4 Feat: Quiz 클래스 구현
* 842288c Feat: Ctrl+C, EOF 종료 처리
* 98faf05 Feat: 메뉴 기능 구현
* c620848 프로젝트 초기 설정
* 579c3b5 Add .gitignore
