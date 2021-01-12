"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

from random import randint

lst = [randint(1, 1000) for i in range(20)]
print(lst)

def generator(lst):
    for i in range(len(lst)):
        if i > 0:
            if lst[i] > lst[i-1]:
                yield lst[i]


new_l = generator(lst)
new_lst = []
for el in new_l:
    new_lst.append(el)

print(new_lst)