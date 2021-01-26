"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if(self.speed >= 60):
            print('Over speed. Speed limit 60')
        return self.speed

class WorkCar(Car):
    def show_speed(self):
        if(self.speed >= 40):
            print('Over speed. Speed limit 40')
        return self.speed

class SportCar(Car):
    def show_speed(self):
        if(self.speed < 200):
            print('Too slow. Go go go')
        return self.speed

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

print('*' * 20)
tc = TownCar(70, 'red', 'Cab')
print(f'Town car: {tc.color} {tc.name} goes with {tc.show_speed()}')

print('*' * 20)
sc = SportCar(170, 'yellow', 'Lamba')
print(f'Sport car: {sc.color} {sc.name} goes with {sc.show_speed()}')

print('*' * 20)
pc = PoliceCar(60, 'black', 'Ford')
print(f'Police car ({pc.is_police}): {pc.color} {pc.name} goes with {pc.show_speed()}')

print('*' * 20)
wc = WorkCar(41, 'gray', 'Kamaz')
print(f'Work car: {wc.color} {wc.name} goes with {wc.show_speed()}')