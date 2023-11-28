numbers = [1,2,3,4,5,6,7,8,9,10]
total = len(numbers)

i = 0
while i < total:
    if numbers[i] % 2 == 0:
        print(numbers[i], "는 짝수 입니다")
    i = i+1