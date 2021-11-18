'''4. Начните работу над проектом «Склад оргтехники». 
    Создайте класс, описывающий склад. 
    А также класс «Оргтехника», который будет базовым для классов-наследников. 
    Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
    В базовом классе определить параметры, общие для приведенных типов. 
    В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class Warehouse:
    def __init__(self, volume):
        self.volume = volume
        self.office_equipments = list()

class OfficeEquipment:
    def __init__(self, length, width, height):
        self.name= None
        self.length=length
        self.width=width
        self.height=height
        self.volume=length*width*height

    def __str__(self) -> str:
        return self.name
    

class Printer(OfficeEquipment):
    def __init__(self, length, width, height, speed_print):
        super().__init__(length, width, height)
        self.name="Printer"        
        self.speed_print=speed_print

class Scanner(OfficeEquipment):
    def __init__(self, length, width, height, speed_scan):
        super().__init__(length, width, height)
        self.name="Scanner"        
        self.speed_scan=speed_scan

class CopyMachine(OfficeEquipment):
    def __init__(self, length, width, height, speed_copy):
        super().__init__(length, width, height)
        self.name="CopyMachine"
        self.speed_copy=speed_copy


class Task:
    def __init__(self):
        self.data = list()

    def __call__(self):
        print(__doc__)
        print("".join(["=" for i in range(100)]))
        config = (({"def":self.main}))
        return config

    def main(self, value, out):
        warehouse = Warehouse(1000)

        printer = Printer(1,2,3,50)
        scanner = Scanner(4,5,6,80)
        copy_machine = CopyMachine(7,8,9,130)

        print(printer)
        print(scanner)
        print(copy_machine)

main()([Task()()])