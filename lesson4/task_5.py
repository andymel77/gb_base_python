"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
"""

from functools import reduce

lst = [el for el in range(100, 1001, 2)]
print(lst)

def my_func(pr_el, el):
    return pr_el * el

print(reduce(my_func, lst))