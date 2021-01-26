"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

class NoSuchEquipment(Exception):
    def __init__(self, txt_exception):
        print('No such equipment at the store')

class OfficeEquipment:
    id = 0
    def __init__(self, name, manufacturer, color, weight, size, interface = 'USB'):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.weight = weight
        self.size = size
        self.interface = interface
        OfficeEquipment.id += 1

class Printer(OfficeEquipment):
    def __init__(self, name, manufacturer, color, weight, size, interface, printer_type = 'laser', colored = False):
        super().__init__(name, manufacturer, color, weight, size, interface)
        self.printer_type = printer_type
        self.colored = colored
        self.id = super().id

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

class Store:
    data_store = {}
    def __init__(self, name, store_type = 'wholesale'):
        self.name = name
        self.store_type = store_type

    def __str__(self):
        return f'{self.data_store}'

    def put(self, equipment: OfficeEquipment, count = 1):
        if equipment.id in self.data_store:
            self.data_store[equipment.id]['count'] += count
        else:
            _tmp = {}
            _tmp['equipment'] = equipment
            _tmp['count'] = count
            _tmp['department'] = 'Main'
            self.data_store[equipment.id] = _tmp
        return self.data_store
    
    def move_to_department(self, equipment: OfficeEquipment, new_dep: str):
        try:
            if equipment.id in self.data_store:
                self.data_store[equipment.id]['department'] = new_dep
            else:
                raise NoSuchEquipment(f'No such equipment {equipment.name} at the store {self.name}')
        except NoSuchEquipment as e:
            print(e)
        finally:
            return self.data_store

    def department_transfer(self, department):
        pass



p1 = Printer('Recoh', 'China', 'white', 2.5, {'width': 3, 'height': 4, 'depth': 5}, 'USB')
p2 = Printer('Epson', 'China', 'black', 5.5, {'width': 13, 'height': 14, 'depth': 15}, 'WiFi/USB')
x2 = Xerox('Xerox', 'Russia', 'black', 5, {'width': 13, 'height': 14, 'depth': 15}, 'WiFi/USB', speed=3, resource=30000)

print(p1.id, p2.id)
st1 = Store('Store 1')

st1.put(p1, 2)
st1.put(p2, 22)
st1.put(p1, 2)
st1.put(x2, 3)

st1.move_to_department(p2, 'New Dep')
print(st1)
st1.move_to_department(p1, 'New Dep')
print(st1)