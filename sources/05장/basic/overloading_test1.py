class Employee():
    def calcSalary(self, x, y):
        print(x * y)
    def calcSalary(self, x, y, z):
        print(x * y * z)

emp = Employee()
emp.calcSalary(100,200,300)
# emp.calcSalary(100,200)