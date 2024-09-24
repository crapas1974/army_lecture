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

def usage():
    print("마음 속에 1에서 9 아홉개의 숫자를 사용한 세 자리 숫자를 하나 정하세요.")
    print("컴퓨터가 3개의 숫자를 제시하면 당신은 다음과 같이 답변합니다.")
    print("자리와 숫자가 모두 맞으면 하나의 스트라이크이며, 숫자는 맞지만 자리가 틀리면 볼 입니다.")
    print("nS nB 형식으로 답변합니다. 예를 들어 2스트라이크 0볼이면 2S 0B입니다.")
    print("3S 0B이면 게임이 종료되며, 이 때까지 반복합니다.")

def interaction(computer_choice, debug = False):
    computer_choice_string = "".join([str(x) for x in computer_choice])
    print("컴퓨터가 선택한 숫자 : ", computer_choice_string)
    user_input = input("당신의 답변을 입력하세요 : ")
    if len(user_input) == 0:
        return 0, 0
    
    user_input_list = user_input.split(" ")
    strike, ball = 0, 0
    for user_input in user_input_list:
        if user_input[1] == 'S':
            strike = int(user_input[0])
        elif user_input[1] == 'B':
            ball = int(user_input[0])
    return strike, ball

def ending(trial):
    print(f"컴퓨터가 {trial}번 만에 맞췄습니다.")

def main():
    trial = 1
    possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    already_chosen = []
    debug_flag = True
    usage()
    input("마음 속에 숫자를 정했다면 엔터를 눌러주세요.")
    if debug_flag:
        user_input = input("Debugging Mode] 정한 숫자를 입력하세요.")
    while True:
        while True:
            computer_choices = random.sample(possible_numbers, 3)            
            if computer_choices not in already_chosen:
                already_chosen.append(computer_choices)
                break
        print(f"----- {trial}번째 시도 -----")
        strike, ball = interaction(computer_choices, debug_flag)
        if strike == 3:
            ending(trial)
            return
        elif strike + ball == 0:
            possible_numbers.remove(computer_choices[0])
            possible_numbers.remove(computer_choices[1])
            possible_numbers.remove(computer_choices[2])
        elif strike + ball == 3:
            possible_numbers = computer_choices
        trial += 1
    

    
    



if __name__ == "__main__":
    main()
