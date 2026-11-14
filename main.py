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
            print("퀴즈 풀기는 준비 중입니다.")
        elif choice == "2":
            print("퀴즈 추가는 준비 중입니다.")
        elif choice == "3":
            print("퀴즈 목록은 준비 중입니다.")
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
