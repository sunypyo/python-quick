from multipledispatch import dispatch

class Employee():
    @dispatch(int, int)
    def calcSalary(x, y):
        print(x * y)

    @dispatch(int, int, int)
    def calcSalary(x, y, z):
        print(x * y * z)

    @dispatch(float, float)
    def calcSalary(x, y):
        print(x * y)

emp = Employee()
emp.calcSalary(100,200)
emp.calcSalary(100,200,300)
emp.calcSalary(400.0, 500.0)