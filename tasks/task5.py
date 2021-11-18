'''5. Продолжить работу над первым заданием. 
    Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. 
    Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class Warehouse:
    def __init__(self, volume):
        self.volume = volume
        self.items = list()

    def item_add(self, item):
        if (self.volume - item.volume) < 0:
            print("Недостаточно места на складе, элемент оргтехники не добавлен!")
            return -1

        self.volume -= item.volume
        self.items.append({"id":len(self.items) + 1,"item":item, "subdivision":"Warehouse"})
        return len(self.items)

    def item_move(self, id, affiliation):
        try:
            index=id-1
            if self.items[index]["subdivision"]!=affiliation:
               print("id: {0}, name: {1}, moved: from {2} to {3}".
               format(self.items[index]["id"],self.items[index]["item"],self.items[index]["subdivision"],affiliation))                
               self.items[index]["subdivision"]=affiliation
               if affiliation=="Warehouse":
                    self.volume -= self.items[index]["item"].volume
               else:
                    self.volume += self.items[index]["item"].volume
        except:
            pass

    def __str__(self) -> str:
        return "\n".join(["id: {0}, name: {1}, subdivision: {2}".format(i["id"],i["item"],i["subdivision"]) for i in self.items])

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

        warehouse.item_add(printer)
        warehouse.item_add(scanner)
        warehouse.item_add(copy_machine)

        print(warehouse)
        warehouse.item_move(2,"IT")

main()([Task()()])