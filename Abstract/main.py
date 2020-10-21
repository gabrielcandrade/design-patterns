from abc import ABCMeta, abstractmethod

# Fabrica geral
class CarroFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_pneu(self):
        pass

    @abstractmethod
    def create_motor(self):
        pass

# Tipo 1
class CarroPopular(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self, carro):
        pass

# Tipo 2
class CarroLuxuoso(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, carro):
        pass

# Estilo 1
class PopularFactory(CarroFactory):
    def create_pneu(self):
        return PneuPopular()

    def create_motor(self):
        return MotorPopular()

# Estilo 2
class LuxuosoFactory(CarroFactory):
    def create_pneu(self):
        return PneuLuxuoso()

    def create_motor(self):
        return MotorLuxuoso()

# Item Popular 1
class PneuPopular(PopularFactory):
    def prepare(self):
        print("Vamos construir o pneu:", type(self).__name__)

# Item Popular 2
class MotorPopular(PopularFactory):
    def serve(self, carro):
        print(
            type(self).__name__,
            ", vai sair um motor do carro popular de",
            type(carro).__name__,
        )

# Item Luxuoso 1
class PneuLuxuoso(LuxuosoFactory):
    def prepare(self):
        print("Vamos construir o pneu TOP:", type(self).__name__)

# Item Luxuoso 2
class MotorLuxuoso(LuxuosoFactory):
    def serve(self, carro):
        print(
            type(self).__name__,
            ", vai sair um motor do carro luxuoso de",
            type(carro).__name__,
        )

# Loja de Carros
class CarStore:
    def make_cars(self):
        for factory in [PopularFactory(), LuxuosoFactory()]:
            motor = factory.create_motor()
            pneu = factory.create_pneu()
            pneu.prepare()
            motor.serve(pneu)

if __name__ == "__main__":
    carro = CarStore()
    carro.make_cars()