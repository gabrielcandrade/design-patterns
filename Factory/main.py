from abc import ABCMeta, abstractmethod


class Sessao(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class SessaoPessoal(Sessao):
    def describe(self):
        print("Sessao Pessoal")


class SessaoFotos(Sessao):
    def describe(self):
        print("Sessao de Fotos")


class SessaoCertificados(Sessao):
    def describe(self):
        print("Sessao de Certificados")


class SessaoPublicacoes(Sessao):
    def describe(self):
        print("Sessao de publicacoes")


class Perfil(metaclass=ABCMeta):
    def __init__(self):
        self.sessoes = list()
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_sessao(self):
        return [type(s).__name__ for s in self.sessoes]

    def add_sessao(self, sessao):
        self.sessoes.append(sessao)


class Linkedin(Perfil):
    def criar_perfil(self):
        self.add_sessao(SessaoPessoal())
        self.add_sessao(SessaoCertificados())
        self.add_sessao(SessaoPublicacoes())


class Facebook(Perfil):
    def criar_perfil(self):
        self.add_sessao(SessaoPessoal())
        self.add_sessao(SessaoFotos())


if __name__ == "__main__":

    linkedin = Linkedin()
    facebook = Facebook()

    print("Criando Perfil...", type(linkedin).__name__)
    print("Perfil tem as sessoes --", linkedin.get_sessao())

    print("Criando Perfil...", type(facebook).__name__)
    print("Perfil tem as sessoes --", facebook.get_sessao())