# class1.py
# 1)클래스 형식을 정의
class person:
    #생성자(초기화)매서드
    def __init__(self):
        #인스턴스의 멤버 변수를 초기화
        self.name = "default name"
    def print(self):
        print("my name is {0}".format(self.name))

# 2)인스턴스 생성
p1 = person()
p1.print()
p2 = person()
p2.name = "전우치"
p2.print()

person.title = "new title"
print(p1.title)
print(p2.title)
print(person.title)
