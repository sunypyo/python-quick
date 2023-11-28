import csv

fruits = ["사과", "파인애플", "배", "복숭아"]
numbers = [50,20,30,60]
values = [1500, 5000, 2500, 2000]

f = open("csv_write_result1.csv", 'w')

try:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(('번호', '과일', '판매수량', '가격', '판매금액'))

    # fruits  리스트의 개수
    num = len(fruits)
    for i in range(num):
        # 리스트 인덱싱을 통해서 각 값들을 읽어온 후 파일에 쓰기
        writer.writerow((i + 1, fruits[i], numbers[i], values[i], (numbers[i] * values[i])))
finally:
    f.close()

# 앞서 만든 파일로 부터 읽어서 출력
print(open('csv_write_result1.csv').read())
f = open('csv_write_result2.csv', 'w')

csv_writer = csv.writer(f, lineterminator='\n')
csv_writer.writerow(['첫번째', '두번째', '세번째'])
csv_writer.writerow(['123', '456', '789'])
csv_writer.writerow(['test', 'hello', 'hi'])

f.close()