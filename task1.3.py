"""
проверка на положительность часов и ставки
"""


class NonNegative:

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f'below zero {self.my_attr} ')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    hours = NonNegative()
    rate = NonNegative()

    def __init__(self, name, surname, hours, rate):
        self.name = name
        self.surname = surname
        self.hours = hours
        self.rate = rate


z = Worker('ilia', 'kvetenadze', 2, 5)
print(z.__dict__)
