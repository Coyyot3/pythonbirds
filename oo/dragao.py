class Dragao:
    pernas = 2 #isso é um atributo de classe, aqui altera quando todos tem 2 pernas.

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
    gordo.pernas = 5    #especifico para essea pessoa!
    del gordo.pernas
    print(cleiton.__dict__)
    print(gordo.__dict__)
    Dragao.pernas = 12 # Assim muda para todos, tem q ser depois do __dict__!(Aqui altera na classe).
    print(Dragao.pernas)
    print(cleiton.pernas)
    print(gordo.pernas)
    print(id(Dragao.pernas))
