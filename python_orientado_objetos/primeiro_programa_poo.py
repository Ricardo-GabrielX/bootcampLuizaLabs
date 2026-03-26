class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    def buzizar(self):
        print('Buzinando...')
    def parar(self):
        print('Parando...')
    def correr(self):
        print('Correndo...')
