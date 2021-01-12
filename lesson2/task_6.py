"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""

goods = []
num = 1

while True:
    try:
        name = input(f'Enter #{num} good name: ')
        price = float(input(f'Enter #{num} good price: '))
        quantity = int(input(f'Enter #{num} good quantity: '))
        unit = input(f'Enter #{num} good unit: ')
        good = (num, {"название": name, "цена": price, "количество": quantity, "ед": unit})
        goods.append(good)
        num += 1
    except ValueError as ex:
        print(ex)
        continue
    finally:
        new = input('Enter another new good (YES/no): ')
        if new.lower() == 'no':
            break

print('Added goods:', goods)

names = set()
prices = set()
qualities = set()
units = set()

for good in goods:
    good_lst = list(good)
    names.add(good_lst[1]['название'])
    prices.add(good_lst[1]['цена'])
    qualities.add(good_lst[1]['количество'])
    units.add(good_lst[1]['ед'])

analytics = {}
analytics['название'] = list(names)
analytics['цена'] = list(prices)
analytics['количество'] = list(qualities)
analytics['ед'] = list(units)
print('Analytics:', analytics)