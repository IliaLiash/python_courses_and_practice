'''
Напишите функцию f_map, которая будет принимать функцию и список значений, а возвращать список в котором каждое значение будет результатом применения переданной функции к переданному списку.
'''

def f_map(func, l):
    for i in range(len(l)):
        l[i] = func(l[i])
    return l