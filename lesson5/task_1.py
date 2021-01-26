"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

with open('my_file_task1.txt', 'w', encoding='utf-8') as file:
    while True:
        str_to_file = input('Enter string: ')
        
        if not str_to_file:
            break

        print(f'{str_to_file}', file=file)