"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time

class TrafficLight:

    _interval = 7

    def __init__(self):
        self.__color = 'red'

    def set_next_color(self):
        print(f'Light {self.__color}')
        if self.__color == 'red':
            self.__color = 'yellow'
            self._interval = 7
        elif self.__color == 'yellow':
            self._interval = 2
            self.__color = 'green'
        else:
            self.__color = 'red'
            self._interval = 5

    def running(self):
        while True:
            self.set_next_color()
            time.sleep(self._interval)

light = TrafficLight()

light.running()