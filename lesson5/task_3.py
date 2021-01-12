"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""

from functools import reduce 

def middle_salary(pr_el, el):
    return pr_el + el

salary = {}

with open('my_file_task3.txt', 'r', encoding='utf-8') as file:
    salary = {line.split()[0]: float(line.split()[1]) for line in file.readlines() if float(line.split()[1]) < 20000}
    for key, val in salary.items():
        print(f'Employee {key} has salary: {val}')

    print(f'Middle salary is {reduce(middle_salary, salary.values())/len(salary.values())}')
    