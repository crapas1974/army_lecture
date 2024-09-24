import random

# 이전 숫자 기준으로 주어진 리스트가 연속된 숫자이면 True
# 빈 리스트 --> False
# 이전 숫자에서 연속이 아니면 --> False
# 이전 숫자에서 연속이면 True
#   숫자가 하나인 경우와 둘 이상인 경우를 구분해서 확인
def is_consecutive(before, numbers):
    if numbers == []:
        return False
    if before + 1 != numbers[0]:
        return False
    else:
        if len(numbers) == 1:
            return True
        
    for i in range(len(numbers) - 1):
        if numbers[i] + 1 != numbers[i + 1]:
            return False
    return True


'''
def is_consecutive(before, numbers):
    if numbers = []:
        return false
    checking_arr = [before] + numbers
    for i in range(len(checking_arr) - 1):
        if checking_arr[i] + 1 != checking_arr[i + 1]:
            return False
    return True
        
'''
# 사용자에게 입력을 받습니다.
def input_user_numbers(current_number):
    while True:
        user_input = input("숫자를 한 개에서 세 개까지 입력하세요. : ")
        if len(user_input.strip()) == 0:
            print("다시 입력해 주세요.")
            continue
        else:    
            try:
                numbers_in_string = user_input.split(" ")
                numbers = [int(x) for x in numbers_in_string]
                if not is_consecutive(current_number, numbers):
                    print("입력한 숫자는 연속된 숫자가 아닙니다.")
                    continue
                if len(numbers) > 3:
                    print("숫자는 3개까지만 입력할 수 있습니다.")
                    continue
                if numbers[-1] > 21:
                    print("21을 초과하는 숫자는 입력할 수 없습니다.")
                    continue
                return numbers
            except ValueError:
                print("ERROR) 형식에 맞게 숫자를 입력하세요.")
                print("ERROR) 한 개에서 세 개까지의 연속된 숫자를 한칸 띄워서 입력하세요.")
                print(f"ERROR) 입력 예시 - {current_number + 1} {current_number + 2}")
                continue
            except Exception:
                print("알 수 없는 예외가 발생했습니다.")


def do_21_game():
    current_number = 0
    while True:
        # 사용자 턴
        print(f"현재 숫자는 {current_number} 입니다.")
        user_input = input_user_numbers(current_number)
        current_number = user_input[-1]
        if current_number == 21:
            print("컴퓨터가 이겼습니다.")
            break
        # 컴퓨터 턴
        print(f"현재 숫자는 {current_number} 입니다.")
        computer_choice = []
        while current_number % 4 != 0:
            current_number += 1
            computer_choice.append(str(current_number))
        print(f"컴퓨터가 선택한 숫자는 {" ".join(computer_choice)} 입니다.")

if __name__ == "__main__":
    do_21_game()