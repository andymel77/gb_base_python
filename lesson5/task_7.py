"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json

firms = {}
av_profit = {}

result = []

with open('my_file_task7.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        res = line.split()
        profit = float(res[2])-float(res[3])
        firms[res[0]] = profit

    av_profit_lst = [val for val in firms.values() if val >= 0]
    av_profit['average_profit'] = round(sum(av_profit_lst) / len(av_profit_lst), 2)

    result.append(firms)
    result.append(av_profit)

with open('my_file_task7.json', 'w', encoding='utf-8') as json_file:
    json.dump(result, json_file)