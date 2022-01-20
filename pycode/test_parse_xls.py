import xlrd

workbook = xlrd.open_workbook(r'C:\Users\Jack\Desktop\api_hub.xls')

sheet1_name = workbook.sheet_names()[0]

print(sheet1_name)

sheet1 = workbook.sheet_by_name(sheet1_name)

print(sheet1.name, sheet1.nrows, sheet1.ncols)

rows =  sheet1.row_values(0)
print(rows[0])

cols = sheet1.col_values(0)
print(cols)
