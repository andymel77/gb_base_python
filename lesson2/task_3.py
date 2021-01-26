"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

seasons = {
    'winter': [12, 1, 2],
    'spring': [3, 4, 5],
    'summer': [6, 7, 8],
    'autumn': [9, 10, 11]
}

try:
    while True: 
        month = int(input('Enter month: '))
        if month in range(1, 13):
            break
        else:
            print(f'{month} is not in range from 1 to 12')
    
    if month in winter:
        print('It\'s winter now')
    elif month in spring:
        print('It\'s spring now')
    elif month in summer:
        print('It\'s summer now')
    elif month in autumn:
        print('It\'s autumn now')

    for key, value in seasons.items():
        if month in value:
            print(f'It\'s {key} now')

except ValueError as ex:
    print(ex)