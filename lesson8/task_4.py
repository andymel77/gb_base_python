"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""

class Store:
    def __init__(self, name, store_type = 'wholesale'):
        self.name = name
        self.store_type = store_type

class OfficeEquipment:
    def __init__(self, name, manufacturer, color, weight, size, interface = 'USB'):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.weight = weight
        self.size = size
        self.interface = interface

class Printer(OfficeEquipment):
    def __init__(self, name, manufacturer, color, weight, size, interface, printer_type = 'laser', colored = False):
        super().__init__(name, manufacturer, color, weight, size, interface)
        self.printer_type = printer_type
        self.colored = colored

class Scanner(OfficeEquipment):
    def __init__(self, name, manufacturer, color, weight, size, interface, scanner_kind = 'handed', scanner_type = 'industrial'):
        super().__init__(name, manufacturer, color, weight, size, interface)
        self.scanner_kind = scanner_kind
        self.scanner_type = scanner_type

class Xerox(OfficeEquipment):
    def __init__(self, name, manufacturer, color, weight, size, interface, speed, format = 'A4', resource = 10000):
        super().__init__(name, manufacturer, color, weight, size, interface)
        self.format = format
        self.speed = speed
        self.resource = resource