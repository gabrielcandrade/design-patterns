class MetaSingleton(type):

    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super(MetaSingleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instancias[cls]


class Logger(metaclass=MetaSingleton):
    def __init__(self, x):
        self.x = x


class Singleton1:

    __instancia = None

    def __new__(cls, nome):
        if Singleton1.__instancia is None:
            Singleton1.__instancia = object.__new__(cls)
            Singleton1.__instancia.__nome = nome
        return Singleton1.__instancia

    @property
    def nome(self):
        return self.__nome


class Singleton2:
    def __new__(cls, nome):
        if not hasattr(cls, "instance"):
            cls.instance = super(Singleton2, cls).__new__(cls)
            cls.instance.__nome = nome
        return cls.instance

    @property
    def nome(self):
        return self.__nome


if __name__ == "__main__":

    foo = Singleton1("Maria")
    print(foo.nome)
    print(foo)

    bar = Singleton1("Joao")
    print(bar.nome)
    print(bar)

    print(foo is bar)

    foo = Singleton2("Maria")
    print(foo.nome)
    print(foo)

    bar = Singleton2("Joao")
    print(bar.nome)
    print(bar)

    print(foo is bar)

    # Example using metaclass
    logger1 = Logger(1)
    logger2 = Logger(2)

    # Nesses prints, veremos que teremos o mesmo object para ambos os Loggers, porque o mesmo esta sendo reaproveitado, nao criado um novo.
    print(logger1)
    print(logger1.x)
    print(logger2)
    print(logger2.x)