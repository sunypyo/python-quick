import xlsxwriter

#Workbook 객체를 생성하고, 워크 시트를 추가한다
# TODO
workbook = xlsxwriter.Workbook('result_excel_case.xlsx')
worksheet = workbook.add_worksheet()

#bar chart를 추가한다
# TODO
chart = workbook.add_chart({'type' : 'bar'})

# 2차원 리스트 형태로 데이터가 제공
# 중첩 리스트 [ [...] , [...], [...] ]
# 표 형식의 2차원 배열
items = [
    ['년도', '2019', '2020', '2021', '2022'],
    ['수익', 3000, 5000, 5500, 6000],
    ['매출 원가', 1500, 3000, 2000, 3000],
    ['이익', 1500, 2000, 3500, 3000]
]

# write_row() --> 2차원 리스트에 한 행씩 꺼내서 행단위로 write
# TODO
# 반복문 미사용 코드
# worksheet.write_row('A1', items[0])
# worksheet.write_row('A2', items[1])
# worksheet.write_row('A3', items[2])
# worksheet.write_row('A4', items[3])

# 반복문 사용
# items 의 전체 행의 개수를 파악
row = len(items)
# 행의 개수만큼 반복하면서 2차원 리스트에서 한 행씩 꺼내어 행단위로 write
for r in range(row): # 0~3 까지 반복
    # worksheet.write_row('A1', items[0])
    # A1 의 형식으로 지정. r 은 0 부터 시작하므로 r+1
    worksheet.write_row( 'A'+str(r+1) , items[r] )

#차트에 데이터를 추가
# TODO
# '=Sheet1!$B$2:$B$4'
series_datas = ['=Sheet1!$B$2:$B$4', '=Sheet1!$C$2:$C$4',
                '=Sheet1!$D$2:$D$4', '=Sheet1!$E$2:$E$4']
# 첫번째 행의 열의 개수
first_row = len(items[0])
# 첫번째 행의 열의 개수만큼 반복하면서 열(셀)을 하나씩 꺼낸다
for r in range(first_row):
    # '년도' 라는 첫번째 열을 건너뛰기
    # items[0][0] 은 건너뛰고,
    # items[0][1] ~ items[0][4] 까지 가져온다
    # name(범례) 로 설정 --> 'name':items[0][r]
    # 결과적으로는 2019 ~ 2022 까지 가져온다
    if r == 0:
        continue
    print(items[0][r])

    # series_datas[r-1] 이라고 한 이유는 series_datas[0] 부터
    # 가져와야 하는데, r 이 0 일때는 continue 했으므로
    # 다음번 반복 횟수로 건너뛰었으므로, r 은 1로 증가해 있다
    chart.add_series({'values': series_datas[r-1],'name': items[0][r]})
    print({'values': series_datas[r-1], 'name': items[0][r]})

    # 코드 참고--> 반복문 미사용 코드
    # chart.add_series({'values': '=Sheet1!$B$2:$B$4', 'name':'2019'})
    # chart.add_series({'values': '=Sheet1!$C$2:$C$4', 'name':'2020'})
    # chart.add_series({'values': '=Sheet1!$D$2:$D$4', 'name':'2021'})
    # chart.add_series({'values': '=Sheet1!$E$2:$E$4', 'name':'2022'})

# 차트 추가
worksheet.insert_chart('A8', chart)

# 수식으로 증가율 추가
# TODO
formulas = ['증가율', '=(B4/B2)*100',
            '=(C4/C2)*100', '=(D4/D2)*100', '=(E4/E2)*100']

col = 0
for formula in formulas:
    worksheet.write(5, col, formula)
    # col = col+1
    col += 1

workbook.close()

