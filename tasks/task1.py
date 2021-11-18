'''1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
    В рамках класса реализовать два метода. 
    Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
    Проверить работу полученной структуры на реальных данных.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class Date:
    date="0-0-0"
    day=0
    hour=0
    year=0

    def __init__(self, date):
        Date.date = date

    @classmethod
    def parse_data(cls):
        values = cls.date.split("-")
        cls.day = int(values[0])
        cls.hour = int(values[1])
        cls.year = int(values[2])

    @staticmethod
    def is_valid(date):
        values = date.split("-")
        if len(values)!=3:
            return False
        try:
            day = int(values[0])
            month = int(values[1])
            year = int(values[2])
        except:
            return False
        return True
        

class Task:
    def __call__(self):
        print(__doc__)
        print("".join(["=" for i in range(100)]))
        config = (({"def":self.main}))
        return config

    def main(self, value, out):
        # Выведем исходный день класса
        Date.parse_data()
        print(Date.day, Date.hour, Date.year)

        dt=Date("10-12-2021")
        Date.parse_data()
        print(Date.day, Date.hour, Date.year)

        data_string="10-12-2021"
        print(Date.is_valid(data_string))

        data_string="10122021"
        print(Date.is_valid(data_string))

        data_string="aa-12-2021"
        print(Date.is_valid(data_string))


main()([Task()()])