dept = input("일반, 영업, 개발 혹은 기타 직군을 입력하세요.")
base_salary = 0

if dept == "일반":
    base_salary = 3000000
elif dept == "영업":
    base_salary = 3500000
elif dept == "개발":
    base_salary = 4000000
else:
    base_salary = 2000000

print("입력하신 직군과 기본급은 다음과 같습니다.")
print(dept, "직군의 기본급은 ", base_salary)