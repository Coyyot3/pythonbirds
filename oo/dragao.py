class Dragao:
    def __init__(self, *filhos, nome = None, idade = 29):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'


if __name__ == '__main__':
    cleiton = Dragao(nome ='Cleiton')
    gordo = Dragao(cleiton, nome ='Gordo')
    print(Dragao.cumprimentar(gordo))
    print(id(gordo))
    print(gordo.cumprimentar())
    print(gordo.nome)
    print(gordo.idade)
    for filho in gordo.filhos:
        print(filho.nome)
    gordo.sobrenome = 'GordaUm'
    del gordo.filhos
    print(cleiton.__dict__)
    print(gordo.__dict__)

[]