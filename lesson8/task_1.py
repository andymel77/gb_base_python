"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""

import datetime

class Date:
    date_str = ''
    def __init__(self, date_str):
        Date.date_str = date_str

    @classmethod
    def get_date_number(cls):
        day, month, year = cls.date_str.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def validate():
        day, month, year = Date.get_date_number()
        now_year = datetime.datetime.now().year
        if day not in range(1, 31):
            raise Exception('Day not in range 1 to 31')
        if month not in range(1, 13):
            raise Exception('Month not in range 1 to 12')
        if year not in range(1, now_year + 1):
            raise Exception(f'Year not in range 1 to {now_year}')


string = '30-12-1977'

d1 = Date(string)

try:
    d1.validate()
except Exception as e:
    print(e)
else:
    print(d1.get_date_number())
