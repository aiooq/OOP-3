'''2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. 
    Проверьте его работу на данных, вводимых пользователем. 
    При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''

import sys
from os.path import dirname
sys.path.append(dirname(dirname(__file__)))
from include.main import Manager as main

class DivisionByZiroError(Exception):
    def __init__(self):
        print("Введен 0, что некорректно, пожалуйста повторите!")
        
    def __str__(self):
        return "Repeat"

class Task:
    def __call__(self):
        print(__doc__)
        print("".join(["=" for i in range(100)]))
        config = (({"in":"Введите число для знаменателя: ","out":"ОК! Спасибо!", "type:":{int,float}, "def":self.main}))
        return config

    def main(self, value, out):
        try:
            print(10/float(value))
        except ZeroDivisionError:
            raise DivisionByZiroError
        return out


main()([Task()()])