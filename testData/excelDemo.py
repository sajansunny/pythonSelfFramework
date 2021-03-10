import openpyxl

book = openpyxl.load_workbook("C:\\Users\\admin\\Documents\\TestData\\HomePageTestData.xlsx")
sheet = book.active
cell = sheet.cell(row=1, column=2)
print(cell.value)

sheet.cell(row=4, column=2).value = "Sunny"
print(sheet.cell(row=4, column=2).value)

print(sheet.max_row)
print(sheet.max_column)

print(sheet['D3'].value)

for i in range(1, sheet.max_row+1):
    print(sheet.cell(row=i, column=1).value)


