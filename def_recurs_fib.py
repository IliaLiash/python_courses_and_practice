'''
Напишите функцию, которая будет вычислять числа Фибоначчи, вызывая саму себя. На всякий случай напоминаю вам формулу:
'''


def fib(n):
    if n == 0 or n==1 or n==2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)