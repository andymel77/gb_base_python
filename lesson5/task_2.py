"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open('my_file_task2.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f'Count of lines: {len(lines)}')
    for i, line in enumerate(lines, 1):
        print(f'At string #{i} {len(line.split())} words')
    