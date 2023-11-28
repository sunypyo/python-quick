# 1. 클래스의 선언 및 정의
class Employee:
    name = '써니'
    # 코드 추가
    tilte = "퀵스타트"
    def prName(self):
        print("이름은 {0} 입니다.".format(self.name))
    # 코드 추가
    def prTitle(self, name, tilte):
        print("prTitle 메서드 호출입니다.")
        print("이름은 {0} 입니다.".format(self.name))
        print("제목은 {0} 입니다.".format(self.tilte))
        print("인자값으로 전달받은 값으로 변경")
        self.name = name
        self.tilte = tilte
        print("변경 후 이름: ", self.name)
        print("변경 후 제목: ", self.tilte)

# 2. 클래스로부터 객체를 생성
emp = Employee()
# 3. 객체를 통해 변수나 함수 사용
emp.prName()
emp.prTitle("파이썬", "클래스의 이해")

# 코드 추가. emp2변수에 emp변수 할당
emp2 = emp
print("emp2에 emp를 할당")
emp2.name = "emp2에서 할당한 이름"
print(emp.name)
