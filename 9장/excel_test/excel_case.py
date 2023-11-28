import xlsxwriter

#Workbook 객체를 생성하고, 워크 시트를 추가한다
workbook = xlsxwriter.Workbook('result_excel_case.xlsx')
worksheet = workbook.add_worksheet()

#bar chart를 추가한다
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
row = len(items)
for r in range(row):
    worksheet.write_row('A' + str(r + 1), items[r])

#차트에 데이터를 추가
series_datas = ['=Sheet1!$B$2:$B$4', '=Sheet1!$C$2:$C$4',
                '=Sheet1!$D$2:$D$4', '=Sheet1!$E$2:$E$4']
first_row = len(items[0])
for r in range(first_row):
    if r == 0:
        continue
    chart.add_series({'values': series_datas[r-1], 'name': items[0][r]})
worksheet.insert_chart('A8', chart)

# 수식으로 증가율 추가
formulas = ['증가율', '=(B4/B2)*100', '=(C4/C2)*100', '=(D4/D2)*100', '=(E4/E2)*100']
col = 0
for formula in formulas:
    worksheet.write(5, col, formula)
    col += 1

workbook.close()

# 추가적인 설명은 excel_case_commnet.py 파일을 참고한다