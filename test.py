class Human:
    def __init__(self, name):
        self.name = name

class Student(Human):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    def print_name_and_working_place(self):
        print(f"학생 {self.name}은 {self.school}학교에 다닙니다.")



arr = [1, 2, 3]
other_arr = [1, 2, 3]
referenced_arr = arr
print(arr == other_arr)         # 값이 같으므로 True
print(arr == referenced_arr)    # 값이 같으므로 True
print(arr is other_arr)         # 갑이 같아도 다른 객체이므로 False
print(arr is referenced_arr)    # 같은 객체이므로 True

arr.append(4)
print(arr)                      # [1, 2, 3, 4]
print(other_arr)                # [1, 2, 3] -> 다른 객체이므로 arr 변경에 영향을 받지 않음
print(referenced_arr)           # [1, 2, 3, 4] -> 같은 객체이므로 arr 변경에 영향을 받음


def evaluation(x):
    if x:
        print(f"{x}는 Truthy")
    else:
        print(f"{x}는 Falsy")

empty = []
psudo_empty = [[]]
evaluation(empty)        # []는 Falsy
evaluation(psudo_empty)  # [[]]는 Truthy