"""
проверка на положительность длины и ширины
"""


class NonNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f'{self.my_attr} below zero  ')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Road:
    length = NonNegative()
    width = NonNegative()

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def massa(self):
        print(self.length * self.width * 25 * 5)


a = Road(5, 10)
a.massa()
