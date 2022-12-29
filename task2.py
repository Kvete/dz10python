class Singleton(type):
    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
            return cls.__instance
        else:
            return cls.__instance


class A(metaclass=Singleton):
    pass


a1 = A()
a2 = A()
a3 = A()
print(a1)
print(a2)
print(a3)
print('a1 is a2 is a3  =', a1 is a2 is a3)
