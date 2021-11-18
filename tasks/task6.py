'''6. Продолжить работу над вторым заданием. 
    Реализуйте механизм валидации вводимых пользователем данных. 
    Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
        Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

import time, random

class Warehouse:
    def __iter__(self):
        return self

    def __init__(self, volume):
        self.i = 0
        self.volume = volume
        self.items = list()

    def __str__(self) -> str:
        return "\n".join(["id: {0}, name: {1}, subdivision: {2}".format(i["id"],i["item"],i["subdivision"]) for i in self.items])        

    def __next__(self):
        if self.i < len(self.items):
            self.i += 1
            return self.items[self.i-1]
        else:
            raise StopIteration

    def __getitem__(self, key):
          return self.items[key]

    def __len__(self):
        return len(self.items)

    def benchmark(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            return_value = func(*args, **kwargs)
            end = time.time()
            print('[*] Время выполнения: {0} секунд.'.format(end-start))
            return return_value
        return wrapper          

    def item_add(self, item):
        if (self.volume - item.volume) < 0:
            print("Недостаточно места на складе, элемент оргтехники не добавлен!")
            return -1

        self.volume -= item.volume
        self.items.append({"id":len(self.items),"item":item, "subdivision":"Warehouse"})
        return len(self.items) - 1

    @benchmark
    def item_move(self, index, affiliation):
        try:
            if self.items[index]["subdivision"]!=affiliation:
               txt = "id: {0}, name: {1}, from: {2}, to: {3}".format(self.items[index]["id"],self.items[index]["item"],self.items[index]["subdivision"],affiliation)

               print(f"Start moving: {txt}")
               time.sleep(random.randint(1,5))
               print(f"End moving: {txt}")

               self.items[index]["subdivision"]=affiliation
               if affiliation=="Warehouse":
                    self.volume -= self.items[index]["item"].volume
               else:
                    self.volume += self.items[index]["item"].volume
        except:
            pass

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
        config = (({"in":"Введите кол-во принтеров отправляемых на склад: ","type":{int},"def":self.main}))
        return config

    def main(self, value, out):
        warehouse = Warehouse(1000)

        printer = Printer(1,2,3,50)
        # scanner = Scanner(4,5,6,80)
        # copy_machine = CopyMachine(7,8,9,130)

        # warehouse.item_add(printer)
        # warehouse.item_add(scanner)
        # warehouse.item_add(copy_machine)

        for i in range(value):
            warehouse.item_add(printer)

        print(warehouse)

        if(len(warehouse)>=3):
            warehouse.item_move(2,"IT")
            print(warehouse[2])

        for i in warehouse:
            print(str(i["item"]))        

main()([Task()()])