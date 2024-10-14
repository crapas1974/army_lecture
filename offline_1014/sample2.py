'''
숫자의 유효성 검증 함수
파라미터
    number_string : 문자열
반환값
    True : 유효한 숫자
    False : 유효하지 않은 숫자
유효성 기준
    1. 길이는 3
    2. 숫자로만 구성
    3. 0이 포함되어 있지 않음
    4. 중복된 숫자가 없음
'''

def is_valid(number_string):
    if type(number_string) != str:
        return False
    if len(number_string) != 3:
        return False
    if '0' in number_string:
        return False
    for i in range(3):
        if number_string[i] < '0' or number_string[i] > '9':
            return False
    if number_string[0] == number_string[1] or number_string[0] == number_string[2] or number_string[1] == number_string[2]:
        return False
    return True

'''
스트라이크, 볼 판정 함수
파라미터
    target : 정답 숫자 문자열
    guess : 추측 숫자 문자열
반환값
    스트라이크 수, 볼 수
스트라이크의 수
    숫자와 위치가 일치하는 경우
볼의 수
    숫자는 일치하지만 위치가 다른 경우
'''

def count_strikes_and_balls(target, guess):
    strikes = 0
    balls = 0
    if target == guess:
        return 3, 0
    if target[0] == guess[0]:
        strikes = strikes + 1
    elif target[0] == guess[1] or target[0] == guess[2]:
        balls = balls + 1
    if target[1] == guess[1]:
        strikes = strikes + 1
    elif target[1] == guess[0] or target[1] == guess[2]:
        balls = balls + 1
    if target[2] == guess[2]:
        strikes = strikes + 1
    elif target[2] == guess[0] or target[2] == guess[1]:
        balls = balls + 1
    return strikes, balls

# alternative
def count_strikes_and_balls_alternative1(target, guess):
    strikes = 0
    balls = 0
    for i in range(3):
        if target[i] == guess[i]:
            strikes = strikes + 1
        elif target[i] == guess[0] or target[i] == guess[1] or target[i] == guess[2]:
            balls = balls + 1
    return strikes, balls

def main():
    testcase_1 = ["1", "12", "1234", 123, "abc", "101", "112", "121", "199", # False
                   "123"]   # True
    for test in testcase_1:
        print(is_valid(test))

    testcase_2 = [("123", "456"), ("123", "379"), ("123", "317"), ("123", "312"), # 0 strike
                  ("123", "145"), ("123", "513"), ("123", "321"), # 1 strike
                  ("123", "193"), # 2 strike
                  ("123", "123")] # 3 strike
    for test in testcase_2:
        print(count_strikes_and_balls(test[0], test[1]))

if __name__ == "__main__":
    main()