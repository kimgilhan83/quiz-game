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
