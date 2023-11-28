import xlsxwriter

workbook = xlsxwriter.Workbook('result1_excel_chart.xlsx')
worksheet = workbook.add_worksheet()

score = [99, 98, 100, 99, 98, 100]

worksheet.write_column('A1', score)
chart = workbook.add_chart({'type': 'column'})
chart.add_series({'values': '=Sheet1!$A$1:$A$6'})

worksheet.insert_chart('C1', chart)
worksheet.insert_image('A16', 'python-logo.png')
workbook.close()

workbook = xlsxwriter.Workbook('result2_excel_chart.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})

headings = ['과일', '판매량']
data = [
    ['사과', '배', '파이애플'],
    [100, 50, 20]
]

worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])

chart1 = workbook.add_chart({'type': 'pie'})
chart1.add_series({
    'categories': ['Sheet1', 1, 0, 3, 0],
    'values': ['Sheet1', 1, 1, 3, 1]
})

chart1.set_title({'name': '과일 판매량'})
worksheet.insert_chart('D3', chart1)
workbook.close()