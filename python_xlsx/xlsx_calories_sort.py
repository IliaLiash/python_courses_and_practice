'''
Васю назначили завхозом в туристической группе и он подошёл к подготовке ответственно, составив справочник продуктов с указанием калорийности на 100 грамм,
а также содержание белков, жиров и углеводов на 100 грамм продукта.
Ему не удалось найти всю информацию, поэтому некоторые ячейки остались незаполненными (можно считать их значение равным нулю).
Также он использовал какой-то странный офисный пакет и разделял целую и дробную часть чисел запятой.
Таблица доступна по ссылке https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx
Вася хочет минимизировать вес продуктов и для этого брать самые калорийные продукты.
Помогите ему и упорядочите продукты по убыванию калорийности. В случае, если продукты имеют одинаковую калорийность - упорядочите их по названию.
В качестве ответа необходимо сдать названия продуктов, по одному в строке.
'''



import xlrd, xlwt
#открываем файл
rb = xlrd.open_workbook('trekking1.xlsx')

results = {}

#выбираем активный лист
sheet = rb.sheet_by_index(0)

#получаем список значений из всех записей построчно
vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]

#если в таблице пустая ячейка - записываем в нее 0
for element in vals[1:]:
    for cell in element[1:]:
        if cell == '':
            cell += '0' 
        cell = float(cell)
        
#записываем в словарь калорийность:продукт. Если в словаре уже есть калорийность - дописываем через ","        
for i in range(1,len(sheet.col_values(0))):
    if sheet.col_values(1)[i] in results:
        results[sheet.col_values(1)[i]] +=(', '+sheet.col_values(0)[i])
    else:
        results[sheet.col_values(1)[i]] = sheet.col_values(0)[i]
        
#сортируем словарь по ключу-калорийности. Из значений по ключу делаем список, который тоже сортируем
for k, v in sorted(results.items(), reverse=True):
    v = sorted(v.split(', '))  
    print(('\n').join(v))