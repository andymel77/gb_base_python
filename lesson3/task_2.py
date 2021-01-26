"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""

def user_data(name, last_name, birth_date, city, email, phone):
    print(f'Фамилия: {last_name}; Имя: {name}; Год рождения: {birth_date}; Город проживания: {city}; E-mail: {email}; Телефон: {phone}')

user_data(name='Ivanov', last_name='Ivan', birth_date='20/01/1981', city='Moscow', email='ivanov.i@gmail.com', phone='+79889889988')