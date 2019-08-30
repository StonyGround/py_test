import xlrd

wb = xlrd.open_workbook('daily.xls')
print(wb.sheets()[0].nrows)
# from openpyxl import load_workbook
#
# workbook = load_workbook('daily.xls')
# # booksheet = workbook.active                #获取当前活跃的sheet,默认是第一个sheet
# sheets = workbook.get_sheet_names()  # 从名称获取sheet
# booksheet = workbook.get_sheet_by_name(sheets[0])
#
# rows = booksheet.rows
# columns = booksheet.columns
# print(rows)
# 迭代所有的行
# for row in rows:
#     line = [col.value for col in row]

# 通过坐标读取值
# cell_11 = booksheet.cell('A1').value
# cell_11 = booksheet.cell(row=1, column=1).value
