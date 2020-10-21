class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.salario = salario

    @property
    def nome(self):
        return self.__nome


class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, outro_parametro=None):
        super(Desenvolvedor, self).__init__(nome, salario)
        self.__outro_parametro = outro_parametro

    @property
    def outro_parametro(self):
        return self.__outro_parametro


class Designer(Funcionario):
    def __init__(self, nome, salario, mais_um_parametro=None):
        super(Designer, self).__init__(nome, salario)
        self.__mais_um_parametro = mais_um_parametro

    @property
    def mais_um_parametro(self):
        return self.__mais_um_parametro


class Organizacao:
    def __init__(self):
        self.__funcionarios = list()

    def add_funcionario(self, funcionario):
        self.__funcionarios.append(funcionario)

    def total_salarios(self):
        salarios = 0
        for funcionario in self.__funcionarios:
            salarios += funcionario.salario
        return salarios


if __name__ == "__main__":
    joao = Desenvolvedor("Joao da Silva", 1800)
    carla = Designer("Carla Camila", 1900)

    organizacao = Organizacao()
    organizacao.add_funcionario(joao)
    organizacao.add_funcionario(carla)

    print(f"Total salários: {organizacao.total_salarios()}")