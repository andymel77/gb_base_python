"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

from random import randint
from functools import reduce

lst = [randint(1, 1000) for i in range(20)]

with open('my_file_task5.txt', 'w', encoding='utf-8') as file:
    num_string = ''
    for el in lst:
        num_string += f'{el} '

    file.write(num_string.strip())

def summa(pr_el, el):
    return int(pr_el) + int(el)

with open('my_file_task5.txt', 'r', encoding='utf-8') as file:
    lines = file.readline()
    print(reduce(summa, lines.split()))
