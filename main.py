# 한글 입력 후 백스페이스를 눌러도 글자가 깨지지 않게 해 주는 입력 도우미
import readline

# 메뉴 화면을 보여 주는 함수 (레시피에 이름표 붙이기)
def show_menu():
    print("=" * 40)           # "=" 글자를 40번 반복해서 줄 긋기
    print("      경제 퀴즈 게임")
    print("=" * 40)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 40)

# 퀴즈 한 개의 규격표(클래스)
class Quiz:
    # 상품을 찍어 낼 때 자동 실행: 라벨 세 개를 붙인다
    def __init__(self, question, choices, answer):
        self.question = question   # 문제
        self.choices = choices     # 선택지(리스트: 4개)
        self.answer = answer       # 정답 번호(1~4)

    # 기능 1: 문제와 선택지를 화면에 보여 준다
    def show(self):
        print(self.question)
        print()
        # 선택지를 1번부터 번호를 붙여서 하나씩 출력
        for number, text in enumerate(self.choices, 1):
            print(f"{number}. {text}")

    # 기능 2: 입력한 번호가 정답인지 확인해서 True/False를 돌려준다
    def check_answer(self, user_answer):
        return user_answer == self.answer

# 정수를 안전하게 입력받는 함수: 올바른 숫자가 들어올 때까지 계속 묻는다
def read_int(prompt, min_value, max_value):
    while True:
        text = input(prompt).strip()          # 앞뒤 공백 제거

        if text == "":                        # 빈 입력 처리
            print("⚠️ 아무것도 입력하지 않으셨습니다. 숫자를 입력하세요.")
            continue                          # 처음으로 돌아가 다시 묻기

        try:
            number = int(text)                # 글자를 숫자로 변환 시도
        except ValueError:                    # 변환 실패(예: abc)
            print("⚠️ 숫자만 입력할 수 있습니다.")
            continue

        if number < min_value or number > max_value:   # 범위 밖 처리
            print(f"⚠️ {min_value}-{max_value} 사이의 숫자를 입력하세요.")
            continue

        return number                         # 모든 검사를 통과: 숫자를 돌려주고 끝

# 퀴즈를 한 문제씩 출제하고 채점하는 함수 (감독관)
def play_quiz(quizzes):
    # 퀴즈가 하나도 없는 경우: 안내만 하고 돌아간다
    if len(quizzes) == 0:
        print("⚠️ 등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
        return None

    total = len(quizzes)    # 전체 문제 수
    correct = 0             # 맞힌 개수 (점수판, 0에서 시작)
    print(f"\n📝 퀴즈를 시작합니다! (총 {total}문제)")

    # 퀴즈를 하나씩 꺼내면서 번호(1부터)를 같이 붙인다
    for index, quiz in enumerate(quizzes, 1):
        print("-" * 40)
        print(f"[문제 {index}]")
        quiz.show()                                   # 문제와 선택지 출력
        user_answer = read_int("정답 입력: ", 1, len(quiz.choices))

        if quiz.check_answer(user_answer):            # 정답이면 True
            print("✅ 정답입니다!")
            correct += 1                              # 점수판에 1점 추가
        else:
            print(f"❌ 오답입니다. 정답은 {quiz.answer}번입니다.")

    score = correct * 100 // total                    # 100점 만점으로 환산
    print("=" * 40)
    print(f"🏆 결과: {total}문제 중 {correct}문제 정답! ({score}점)")
    print("=" * 40)
    return score                                      # 점수를 돌려준다 (나중에 최고 점수 비교에 사용)

# 등록된 퀴즈 목록을 보여 주는 함수 (재고 목록표)
def show_quiz_list(quizzes):
    # 퀴즈가 하나도 없는 경우
    if len(quizzes) == 0:
        print("⚠️ 등록된 퀴즈가 없습니다.")
        return

    print(f"\n📋 등록된 퀴즈 목록 (총 {len(quizzes)}개)")
    print("-" * 40)
    # 번호(1부터)와 문제만 한 줄씩 출력
    for index, quiz in enumerate(quizzes, 1):
        print(f"[{index}] {quiz.question}")
    print("-" * 40)

# 글자를 안전하게 입력받는 함수: 빈 입력이면 다시 묻는다
def read_text(prompt):
    while True:
        text = input(prompt).strip()          # 앞뒤 공백 제거
        if text == "":                        # 빈 입력 처리
            print("⚠️ 아무것도 입력하지 않으셨습니다. 내용을 입력하세요.")
            continue
        return text


# 새 퀴즈를 입력받아 진열대에 추가하는 함수 (입고 담당자)
def add_quiz(quizzes):
    print("\n📌 새로운 퀴즈를 추가합니다.")
    question = read_text("문제를 입력하세요: ")

    choices = []                              # 빈 리스트(빈 상자)를 준비
    for number in range(1, 5):                # 1, 2, 3, 4를 차례로 반복
        text = read_text(f"선택지 {number}: ")
        choices.append(text)                  # 상자 맨 끝에 하나씩 담기

    answer = read_int("정답 번호 (1-4): ", 1, 4)

    new_quiz = Quiz(question, choices, answer)   # 상품 완성
    quizzes.append(new_quiz)                     # 진열대 맨 끝에 올리기
    print("✅ 퀴즈가 추가되었습니다!")

# 기본 퀴즈 5개를 만들어서 리스트로 돌려주는 함수
def create_default_quizzes():
    return [
        Quiz(
            "물가가 지속적으로 오르는 현상을 무엇이라고 할까요?",
            ["디플레이션", "인플레이션", "스태그플레이션", "리세션"],
            2,
        ),
        Quiz(
            "중앙은행이 물가를 잡기 위해 조정하는 대표적인 수단은?",
            ["법인세", "최저임금", "기준금리", "관세"],
            3,
        ),
        Quiz(
            "1달러가 1,300원에서 1,400원으로 올랐습니다. 원화의 가치는?",
            ["올랐다", "내렸다", "변화 없다", "알 수 없다"],
            2,
        ),
        Quiz(
            "'계란을 한 바구니에 담지 말라'는 투자 격언이 뜻하는 것은?",
            ["집중투자", "단기투자", "레버리지 투자", "분산투자"],
            4,
        ),
        Quiz(
            "원금뿐 아니라 이미 붙은 이자에도 이자가 붙는 방식은?",
            ["복리", "단리", "할인", "상계"],
            1,
        ),
    ]


# 가게 문 열기 전에 기본 퀴즈를 진열대(quizzes)에 올려 둔다
quizzes = create_default_quizzes()



# 영업 시작: 가게 전체를 비상 매뉴얼(try) 안에 둔다
try:
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            play_quiz(quizzes)
        elif choice == "2":
            add_quiz(quizzes)
        elif choice == "3":
            show_quiz_list(quizzes)
        elif choice == "4":
            print("점수 확인은 준비 중입니다.")
        elif choice == "5":
            print("게임을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")

# 비상 매뉴얼: Ctrl+C 또는 Ctrl+D가 눌리면 여기로 온다
except (KeyboardInterrupt, EOFError):
    print("\n입력이 중단되었습니다. 안전하게 종료합니다.")
