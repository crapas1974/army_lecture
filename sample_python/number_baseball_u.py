import random
def input_validation(user_input):
    if len(user_input) != 3:
        print("세 자리 숫자를 입력하세요.")
        return False    
    try:        
        if "0" in user_input:
            raise ValueError("0은 입력할 수 없습니다.")
        if user_input[0] == user_input[1] or user_input[1] == user_input[2] or user_input[0] == user_input[2]:
            raise ValueError("중복된 숫자는 입력할 수 없습니다.")
        number = int(user_input)
    except ValueError as error:
        print("잘못 된 입력입니다. : ", error)
        return False
    return True

def main():
    # 컴퓨터가 숫자 3개를 임의로 선택합니다.
    computer_numbers = random.sample(range(1, 9), 3)
    debug_flag = False
    if debug_flag:
        print(computer_numbers)

    trial = 0
    while True:
        trial += 1
        print(f"----- {trial}번째 시도 -----")
        user_input = input("세 자리 숫자를 입력하세요 : ")
        if not input_validation(user_input):
            print("입력 가이드 : 1 ~ 9 사이의 숫자를 중복없이 선택한 후, 세 자리 숫자로 입력하세요.")
            continue
        strike_count = 0
        ball_count = 0
        for i in range(3):
            if int(user_input[i]) == computer_numbers[i]:
                strike_count += 1
            elif int(user_input[i]) in computer_numbers:
                ball_count += 1
        if strike_count == 3:
            print(f"{trial}번 만에 맞췄습니다!")
            break
        print(f"{strike_count}S {ball_count}B")
                                                                                                            
    print("게임이 종료되었습니다.")

if __name__ == "__main__":
    main()
