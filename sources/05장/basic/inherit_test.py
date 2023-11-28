class Empolyee:
    name = "사원이름"
    salary = 300

    def __init__(self,name):
        self.name = name

    def info(self):
        print("=== 사원 정보 ===")
        print("{0} 님의 정보 입니다.".format(self.name))

    def calcSalary(self):
        print("=== 사원의 월급계산 ===")
        print("사원의 월급은 {0} 입니다.".format(self.salary))

class Manager(Empolyee):
    title = "직책"

    def __init__(self,name, title):
        self.name = name
        self.title = title

    def calcSalary(self):
        print("=== 관리자의 월급계산 ===")

        if self.title == '대리':
            self.salary += 50
        elif self.title == '과장':
            self.salary += 100
        elif self.title == '차장':
            self.salary += 150
        elif self.title == '부장':
            self.salary += 200
        else:
            self.salary += 300

        print("{0}의 월급은 {1} 입니다.".format(self.title, self.salary))


emp = Empolyee("써니")
emp.info()
emp.calcSalary()

mgr = Manager("루나", "과장")
mgr.info()
mgr.calcSalary()

mgr2 = Manager("엘리", "차장")
mgr2.info()
mgr2.calcSalary()