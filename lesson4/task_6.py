"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, cycle

start_number = 2
end_number = 12

for el in count(start_number):
    if el > end_number:
        break
    print(el)

print('#'*20)

lst = [23, 1, 3, 10, 4, 11]

i = 0
for el in cycle(lst):
    if i > end_number:
        break
    print(el)
    i += 1