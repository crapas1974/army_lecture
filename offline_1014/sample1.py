# -> 추가 입력

# 컴퓨터가 가위, 바위, 보 중 하나를 선택하는 함수
# 반환값 : 컴퓨터의 선택 (문자열)
# -> 추가 입력




# 사용자가 가위, 바위, 보 중 하나를 입력하는 함수
# 반환값 : 사용자의 입력 또는 None (입력이 잘못된 경우)
def human_input():
    user_input = input("가위, 바위, 보 중 하나를 입력하세요 :")
    if user_input != "가위" and user_input != "바위" and user_input != "보":
        print("잘못 입력했습니다.")
        return None
    return user_input

# 누가 이겼는지를 판정하는 함수
# 매개변수 : user_choice - 사용자의 선택, computer_choice - 컴퓨터의 선택
# 반환값 : 1 (사용자 승리), 2 (비김), 3 (컴퓨터 승리)
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 2
    if user_choice == "가위" and computer_choice == "보" or user_choice == "바위" and computer_choice == "가위" or user_choice == "보" and computer_choice == "바위":
        return 1
    return 3

# 게임 시작
# 무한 루프 - 사용자 입력이 정상적이면 루프를 종료

computer_win = 0
human_win = 0
trial = 0

# -> 추가 입력

   
   


    




    # 컴퓨터 선택
    computer_choice = computer_select()

    # 선택 출력
    print(f"사용자의 선택 - {user_choice}")
    print(f"컴퓨터의 선택 - {computer_choice}")

    # 결과 확인
    result = determine_winner(user_choice, computer_choice)
    if result == 1:
        print("사용자가 이겼습니다.")
        human_win = human_win + 1
    elif result == 2:
        print("비겼습니다.")
    else:
        print("컴퓨터가 이겼습니다.")
        computer_win += 1
    if debug:
        print(f"사용자: {human_win}승, 컴퓨터: {computer_win}승")

if human_win == 3:
    print(f"{human_win}승 {computer_win}패로 사용자의 승리!")
else:
    print(f"{computer_win}승 {human_win}패로 컴퓨터의 승리!")
