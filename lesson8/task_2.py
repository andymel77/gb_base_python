"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class DivisionByZero(Exception):
    def __init__(self, txt_exception):
        self.txt_exception = txt_exception

try:
    a = int(input('Enter a number a: '))
    b = int(input('Enter a number b: '))
    if b == 0:
        raise DivisionByZero('Can\'t devide by zero')
except ValueError:
    print('Not a number entered')
except DivisionByZero as e:
    print(e)
else:
    print(a/b)