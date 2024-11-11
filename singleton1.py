class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.value = None


class DerivedSingleton(Singleton):
    def set_value(self, value):
        self.value = value

singleton1 = DerivedSingleton()
singleton1.set_value(10)

singleton2 = DerivedSingleton()

print(singleton1 is singleton2)
print(singleton2.value)
