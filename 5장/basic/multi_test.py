class Empolyee:
    def info(self):
        print("일반직 사원 정보")
    def calcSalary(self):
        print("일반직 사원 월급 계산...")

class Sales:
    def sale(self):
        print("영업직 사원 정보")
    def calcSalary(self):
        print("영업 수당 추가 월급 계산....")

class SalesEmployee(Sales, Empolyee):
    def manage(self):
        print("영업 관리 정보")

s = SalesEmployee()
s.info()
s.sale()
s.calcSalary()
s.manage()

print("=== method resolution order ===")
print(SalesEmployee.__mro__)