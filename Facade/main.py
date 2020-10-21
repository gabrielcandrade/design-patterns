class Hoteleiro:
    def __init__(self):
        print("O melhor hotel da cidade!")

    def __is_available(self):
        print("Será que encontramos alguma diária disponível?")
        return True

    def book_hotel(self):
        if self.__is_available():
            print("Data registrada no livro!\n")

class Florista:
    def __init__(self):
        print("Quantas flores serão necessarias para o evento? --")

    def set_flower_requirements(self):
        print("Rosas e Tulipas foram as escolhidas...\n")

class Cozinheiro:
    def __init__(self):
        print("A cozinha será composta por qual prato principal? --")

    def set_cuisine(self):
        print("Comida oriental é nossa especialidade! Pode deixar!\n")

class Musico:
    def __init__(self):
        print("Podem deixar que daremos conta da harmonia! --")

    def set_music_type(self):
        print("Tocamos de Axé a Forró!\n")

class Cerimonialista:
    def __init__(self):
        print("Cerimonialista:: Deixe-me conversar com os fornecedores!\n")

    @staticmethod
    def arrange():
        hoteleiro = Hoteleiro()
        hoteleiro.book_hotel()

        florista = Florista()
        florista.set_flower_requirements()

        cozinheiro = Cozinheiro()
        cozinheiro.set_cuisine()

        musico = Musico()
        musico.set_music_type()


class Cliente:
    def __init__(self):
        print("Cliente:: Uau! Como tudo está bacana! Já está no pacote?")

    def ask_event_manager(self):
        print("Cliente:: Vamos contactar o cerimonialista\n")
        em = Cerimonialista()
        em.arrange()

    def __del__(self):
        print("Cliente:: Obrigado Cerimonialista, tudo ficou excelente!")


if __name__ == "__main__":
    cliente = Cliente()
    cliente.ask_event_manager()