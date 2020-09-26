import xlrd, xlwt
from statistics import median, mean
#открываем файл
rb = xlrd.open_workbook('salaries.xlsx')

#выбираем активный лист
sheet = rb.sheet_by_index(0)

#получаем значение профессий
professions = sheet.row_values(0)[1:]
#получаем значение регионов
regions = sheet.col_values(0)[1:]

#создаем словарь, куда будем записывать регион: значение медианы
medians = {}
#начинаем перебирать строки, добавляя в словарь
for i in range(1,9):
        a = sheet.row_values(i)[1:]
        result = [int(item) for item in a]
        medians[sheet.row_values(i)[0]] = median(result)
#выводим макисмальный элемент из словаря       
for k, v in medians.items():
        if v == max(medians.values()):
                print(k, v)
                break
#аналогичные операции для средней, только действуем с колонками        
average = {}
for i in range(1,8):
        a = sheet.col_values(i)[1:]
        result = [int(item) for item in a]
        average[sheet.col_values(i)[0]] = mean(result)
        
for k, v in average.items():
        if v == max(average.values()):
                print(k, v)
                break