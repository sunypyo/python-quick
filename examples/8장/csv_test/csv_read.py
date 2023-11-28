import csv

# reader() 메서드를 사용하여 CSV file 읽기
# 읽어온 데이터를 파이썬의 리스트로 변환하여 출력하기
f = open('csv_read_test.csv')
try:
    reader = csv.reader(f)
    # 읽어온 데이터를 파이썬의 리스트로 변환하여 출력하기
    print("CSV 로부터 읽어온 파일: ", list(reader))
except Exception as e:
    print("예외 사항 발생 - ", e)
finally:
    f.close()

print("이용가능한 Dialects:", csv.list_dialects())
print("=" * 30)

# csv 파일의 내용을 반복문으로 읽기
f = open("csv_read_test.csv")
try:
    reader = csv.reader(f)
    # 반복문을 사용하여 읽은 내용 출력
    for r in reader:
        print(r)
finally:
    f.close()

print("=" * 30)

#DictReader() 를 사용하여 파이썬 딕셔너리로 읽기
f = open("csv_read_test.csv")
print("파이썬 딕셔너리로 읽기")
try:
    reader = csv.DictReader(f)
    # 전체 파일로 부터 반복하면서 하나의 행씩 꺼내어 r 이라는 임시변수에 담기
    for r in reader:
        # 딕셔너리 키를 주고 value 꺼내어 출력
        print(r['성'], r['이름'], r['이메일'])
finally:
    f.close()

print("=" * 30)