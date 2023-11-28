"""사용자 정의 모듈.
사원의 급여를 출력하는 함수를 제공.
"""

def calc_salary(emp, salary):
    """급여 계산 함수.
    emp : 입력값은 사원 혹은 임원,
    salary : 급여
    사원과 임원의 급여를 계산하여 출력한다."""
    base = 2000000
    extra = 5000000
    if emp == '사원':
        salary = base + salary
    elif emp == '임원':
        salary = base + salary + extra
    print('%s의 급여는 %s 입니다.' % (emp, salary) )

def info(code):
    """사원 정보 출력 함수.
    code : 사원의 코드.
    사원의 코드를 통해 사원과 부서의 정보를 출력한다."""
    if code == "001-001":
        employee = '총무팀 일반직'
    elif code == "001-002":
        employee = '총무팀 관리직'
    elif code == "002-001":
        employee = '개발팀 일반직'
    elif code == "002-002":
        employee = '개발팀 관리직'
    elif code == "003-002":
        employee = '운영팀 일반직'
    elif code == "003-002":
        employee = '운영팀 관리직'
    elif code == "004-001":
        employee = '임원'
    else:
        employee = '기타'
    print('조회하신 사원의 정보입니다.')
    print('%s 코드는 %s 사원입니다.' % (code, employee))

def main():
    print('사원의 급여와 사원 코드의 정보를 모두 출력합니다.')
    calc_salary('사원', 3000000)
    info('001-001')
    calc_salary('임원', 5000000)
    info('004')

if __name__ == "__main__":
    main()
