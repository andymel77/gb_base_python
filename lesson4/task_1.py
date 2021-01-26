"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

try:
    work_hours = float(argv[1])
    rate_per_hour = float(argv[2])
    prize = float(argv[3])
    print(f'Salary: {(work_hours*rate_per_hour)+prize}')
except Exception as ex:
    print('Wrong parameters')

