# class2.py
# 1)클래스 형식을 정의
class person:
    num_person = 0
    #생성자(초기화)매서드
    def __init__(self):
        #인스턴스의 멤버 변수를 초기화
        self.name = "default name"
        person.num_person += 1
    def print(self):
        print("my name is {0}".format(self.name))

# 2)인스턴스 생성
p1 = person()
p2 = person()
p3 = person()
print("인스턴스 갯수:{0}".format(person.num_person))