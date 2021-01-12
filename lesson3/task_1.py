"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def division(a, b):
    try:
        result = a/b
    except ZeroDivisionError as ex:
        print(ex)
        return 0
    except ValueError as ve_ex:
        print(ve_ex)
        return 0
    return result

try:
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(division(a, b))
except ValueError as ve_ex:
    print(ve_ex)

