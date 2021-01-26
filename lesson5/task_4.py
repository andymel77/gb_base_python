"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

numbers = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре'}

with open('my_file_task4_in.txt', 'r', encoding='utf-8') as file_in:
    lines = {line.split(line.split()[1])[0].strip(): numbers[line.split(line.split()[1])[1].strip()] for line in file_in.readlines()}
    
with open('my_file_task4_out.txt', 'w', encoding='utf-8') as file_out:
    for key, val in lines.items():
        print(f'{key} - {val}', file=file_out)
    


