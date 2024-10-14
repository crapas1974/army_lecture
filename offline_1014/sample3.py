from sample2 import is_valid, count_strikes_and_balls
import random

# 정답 숫자를 사용자가 입력
while True:
    target = input('1에서 9 사이의 중복되지 않는 숫자 3개로 구성된 3자리 숫자를 입력하세요: ')
    if is_valid(target):
        break
    else:
        print('잘못 입력했습니다.')

debug = False
tries = 0
possible_digits = [str(i) for i in range(1, 10)]
used_numbers = []
while True:
    # 컴퓨터가 3개의 숫자를 possible_digits에서 랜덤으로 선택
    while True:
        computer_guess = ''
        for _ in range(3):
            computer_guess += random.choice(possible_digits)
        if is_valid(computer_guess) and computer_guess not in used_numbers:
            break
    used_numbers.append(computer_guess)
    strikes, balls = count_strikes_and_balls(target, computer_guess)
    tries += 1
    print(f"{tries}번째 시도에서 컴퓨터는 {computer_guess}라고 추측했고, 결과는 {strikes}S {balls}B 입니다.")
    if strikes == 3:
        break
    if strikes == 0 and balls == 0:
        for number in computer_guess:
            possible_digits.remove(number)
    if strikes + balls == 3:
        possible_digits = list(computer_guess)
    if debug:
        print(f"possible_digits = {possible_digits}")
    
print(f"컴퓨터가 {tries}번째 시도에 맞췄습니다.")
