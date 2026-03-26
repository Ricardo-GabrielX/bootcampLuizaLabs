from abc import ABC, abstractmethod, abstractproperty
import datetime
import textwrap

class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente:Cliente, historico:Historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico() 

    @classmethod
    def nova_conta (cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia 
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def __del__(self):
        print('Conta deletada')

    
    def sacar(self, valor:float):
        if valor > self._saldo:
            print('Saldo insuficiente')
        else:
            self._saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso. Saldo atual: R${self._saldo}')
        
    def depositar(self, valor:float):
        self._saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso. Saldo atual: R${self._saldo}')

class ContaCorrente(Conta):
    def __init__(self, numero, cliente ,limite=500, limite_saques= 3 ):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numeros_saques = len([
            transacao for transacao in self._historico.transacoes if transacao['tipo'] == Saque.__name__])

        excedeu_limite = valor > self._limite
        excedeu_saques = numeros_saques >= self._limite_saques

        if excedeu_limite:
            print('Valor do saque excede o limite.')
        elif excedeu_saques:
            print('Número máximo de saques excedido.')
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f'Número: {self._numero} - Agência: {self._agencia} - Saldo: R${self._saldo:.2f}'


class Cliente:
        def __init__(self, endereco:str, contas:list):
            self._endereco = endereco
            self._contas = []

        def __del__(self):
            print('Cliente deletado')
        
        def realizar_transacao(self, conta: Conta, transacao):
            transacao.registrar(conta)

        def adicionar_conta(self, conta: Conta):
            self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento:str, endereco:str, contas:list):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        

class Historico:
    def __init__(self):
        self._transacoes = []
    
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao: Transacao):
        self._transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        })
        

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass  

    @abstractmethod
    def registrar(conta: Conta):
        pass

class Saque(Transacao):
    def __init__(self, valor:float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        sucesso_transacao = conta.sacar(self._valor)
        if sucesso_transacao:
            conta._historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor:float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta: Conta):
        sucesso_transacao = conta.depositar(self._valor)
        if sucesso_transacao:
            conta._historico.adicionar_transacao(self)
            
    



def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q]\tSair
    =====================================\n
"""
    return input(textwrap.dedent(menu))


def filtar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente._contas:
        print('Cliente não possui conta')
        return None
    
    return cliente._contas[0]


def depositar(clientes):
    cpf = input('Digite o CPF do cliente: ')
    cliente = filtar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado')
        return
    

    valor = float(input('Digite o valor do depósito: '))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input('Digite o CPF do cliente: ')
    cliente = filtar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado')
        return
    
    valor = float(input('Digite o valor do saque: '))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input('Digite o CPF do cliente: ')
    cliente = filtar_cliente(cpf, clientes)

    if not cliente:
        print('Cliente não encontrado')
        return
    
    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    print('\n==========EXTRATO==========='.center(30))
    transacoes = conta.historico.transacoes()
    extrato = ''
    if not transacoes:
        extrato = 'Não foram realizadas movimentações.'
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}: R${transacao['valor']:.2f} - {transacao['data']}\n"

    print(extrato)
    print(f'Saldo: R${conta.saldo:.2f}')
    print('============================'.center(30))




def main():
    clientes = []
    contas = []
    while True:
        opcao = menu()
        
        if opcao == 'd':
            depositar(clientes)

        elif opcao == 's':
            sacar(clientes)

        elif opcao == 'e':
            exibir_extrato(clientes)
        
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
