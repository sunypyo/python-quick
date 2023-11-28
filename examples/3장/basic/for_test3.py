# dict 에서 반복문 사용. 딕셔너리의 각 아이템들을 반복하여 출력한다.
emps = {'선영':500, '길동':100, '지훈':200}
for k,v in emps.items():
    print(k,v)
print("==============")

# 딕셔너리의 키를 하나씩 꺼내와서,
# 키를 가지고 값을 가져와서 출력한다
for key in emps.keys():
    print(key, emps[key])
print("==============")

# set 에서 반복문 사용
s = {1,2,3,3,4,4,5,5}
for i in s:
    print(i, end=' ')
# 출력할때 쭉 한줄에 추가하므로
# 다음줄에 구분선을 추가하려면 \n 을 넣어준다
print("\n==============")

# tuple 에서 반복문 사용
t = (1,2,3,3,4,4,5,5)
for i in t:
    print(i, end=' ')
