'''
В первый год в пруду живет 120 лягушек. Каждый год из пруда вылавливают 50 лягушек, а оставшиеся размножаются и их становится в два раза больше.
Напишите функцию `number_of_frogs(year)` которая будет считать количество лягушек в произвольный год.
'''

def number_of_frogs(year):
    if year == 1:
        return 120
    else:
        return 2 * (number_of_frogs(year - 1) - 50)