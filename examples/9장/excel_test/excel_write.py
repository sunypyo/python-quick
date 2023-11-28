import xlsxwriter

# Workbook 메소드를 사용하여 workbook 객체를 생성
workbook = xlsxwriter.Workbook('result_excel_write.xlsx')
# add_worksheet 메소드를 사용하여 worksheet 객체를 생성
worksheet = workbook.add_worksheet()

# items 2차원 리스트에 데이터를 추가
items = [ 
    ['선영', 1000],
    ['비니',   100],
    ['지훈',  300],
    ['강이',    50]
]

row = 0
col = 0

for item, cost in items:
    worksheet.write(row, col, item)
    worksheet.write(row, col + 1, cost)
    row += 1

worksheet.write(row, 0, 'Total')
worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()