class EstacaoDeRadio:
    def __init__(self, frequencia):
        self.__frequencia = frequencia

    @property
    def frequencia(self):
        return self.__frequencia


class ListaEstacoes:
    def __init__(self):
        self.__estacoes = list()
        self.__contador = 0

    def add_estacao(self, estacao_radio):
        self.__estacoes.append(estacao_radio)

    def remove_estacao(self, frequencia):
        for index in range(0, len(self.__estacoes)):
            if self.__estacoes[index].frequencia == frequencia:
                self.__estacoes.pop(index)
                break
        else:
            print("Estacao de radio nao encontrada.")

    def contador(self):
        return len(self.__estacoes)

    def atual(self):
        return self.__estacoes[self.__contador].frequencia

    def chave(self):
        return self.__contador

    def __next__(self):
        self.__contador += 1

    def rewind(self):
        self.__contador = 0


if __name__ == "__main__":
    lista_de_estacoes = ListaEstacoes()

    lista_de_estacoes.add_estacao(EstacaoDeRadio(89))
    lista_de_estacoes.add_estacao(EstacaoDeRadio(101))
    lista_de_estacoes.add_estacao(EstacaoDeRadio(102))
    lista_de_estacoes.add_estacao(EstacaoDeRadio(103.2))

    print(f"Estacoes: {lista_de_estacoes.contador()}")
    lista_de_estacoes.remove_estacao(89)
    print(f"Estacoes: {lista_de_estacoes.contador()}")

    print(f"Estacao Atual: {lista_de_estacoes.atual()}")
    next(lista_de_estacoes)
    print(f"Estacao Atual: {lista_de_estacoes.atual()}")