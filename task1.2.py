"""
проверка на существование данного цвета
"""


class NonColor:

    def __set__(self, instance, value):
        if value not in ['green', 'red', 'blue', 'yellow', 'brown', 'white',
                         'black']:
            raise ValueError(f'there is no this color: {value}')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Car:
    color = NonColor()

    def __init__(self, speed, color, name, ispolice):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = ispolice

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
        print(f"{self.name} повернула")

    def show_speed(self):
        print(f'cкорость={self.speed}')


a = Car(50, 'yellow', 'reno', False)
print(a.color)
