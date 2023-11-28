import basic.employee as emp

print("==== employee 의 함수 호출 ====")
emp.info('001-001')

print(emp.__name__)

print("==== employee 객체의 dostring 확인 ====")
print(help(emp))
print("==== employee 객체의 info 함수의 dostring 확인 ====")
print(help(emp.info))
print("==== employee 객체의 calc_salary 함수의 dostring 확인 ====")
print(help(emp.calc_salary))