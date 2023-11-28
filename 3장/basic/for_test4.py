# 짝수 구하는 예제에서 동일한 코드를 리스트 내장(list comprehension)를 사용하면
# 더욱 편하고 간단하게 사용할 수 있다.
# 리스트 내장은 결과를 리스트로 준다
numbers = [1,2,3,4,5,6,7,8,9,10]
result = [n for n in numbers if n % 2 ==0]
print(result, "는 짝수 입니다")

print("==============")
# 리스트 내장. 조건문 없이 리스트에서 하나씩 꺼내와서 10을 곱하는 연산을 수행
numbers = [1,2,3,4,5]
result = [num * 10 for num in numbers]
print(result)
print("==============")

# 리스트 내장 없이 for 문을 사용해도 된다
# 다만 이 경우 결과값은 리스트가 아니다
# print() 문을 한 줄 출력으로 사용
for num in numbers:
    print(num * 10, end=' ')
print("\n==============")

# 동일한 코드를 리스트 내장으로 사용
result = [num * 10 for num in numbers if num % 2 == 0]
print(result)
print("=================")

# 문자열로 리스트를 만들어서 리스트 내장을 사용
# 문자열 객체가 가지고 있는 upper() 함수를 호출할 수 있다
# upper() 함수는 모두 대문자로 변경해 주는 함수이다
fruits = ['apple', 'pear', 'cherry', 'grape', 'pineapple']
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)
print("=================")

# 리스트 내장을 사용하지 않고 for 문을 사용하여 동일한 결과를 얻기 위한 코드
fruits = ['apple', 'pear', 'cherry', 'grape', 'pineapple']
# 대문자로 변경한 값들을 저장할 빈 리스트를 선언
upper_fruits = [ ]
for fruit in fruits:
    # 원본 리스트에서 요소를 하나씩 꺼내 대문자로 변경 후 temp 변수에 저장
    temp = fruit.upper()
    # temp 값을 upper_fruits 리스트에 추가(append)
    upper_fruits.append(temp)
print(upper_fruits)