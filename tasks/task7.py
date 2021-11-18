'''7. Реализовать проект «Операции с комплексными числами». 
    Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. 
    Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
    Проверьте корректность полученного результата.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class ComplexNumber(complex):
    def __init__(self, value):
        self.value=value

    def __eq__(self, other) -> bool:
        return isinstance(other,complex)

    def __add__(self, other) -> complex:
        return self.value+other

    def __mul__(self, other) -> complex:
        return self.value*other

class Task:
    def __init__(self):
        self.data = list()

    def __call__(self):
        print(__doc__)
        print("".join(["=" for i in range(100)]))
        config = (({"def":self.main}))
        return config

    def main(self, value, out):

        number_1 = ComplexNumber(2j)
        number_2 = ComplexNumber(10j)

        print(f"{number_1}+{number_2}={number_1+number_2}")
        print(f"{number_1}*{number_2}={number_1*number_2}")

main()([Task()()])