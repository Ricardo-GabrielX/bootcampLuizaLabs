from abc import ABC, abstractmethod
import datetime
import textwrap

class Conta:
    def __init__(self, saldo:float, numero:int, agencia:str, cliente:Cliente, historico:Historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico() 
    
    def __del__(self):
        print('Conta deletada')

    def saldo(self, saldo:float):
        return self._saldo
    
    def nova_conta(self, cliente: Cliente, numero: int):
        self._cliente = cliente
        self._numero = numero
    
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
            self._contas = contas

        def __del__(self):
            print('Cliente deletado')
        
        def realizar_transacao(self, conta: Conta, transacao):
            valor = float(input('Digite o valor da transação: '))
            tipo = input('Digite o tipo da transação (sacar/depositar): ')
            if tipo == 'sacar':
                conta.sacar(valor)
            elif tipo == 'depositar':
                conta.depositar(valor)
            else:
                print('Tipo de transação inválido')

        def adicionar_conta(self, conta: Conta):
            self._contas.append(conta)
            print('Conta adicionada com sucesso')

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
    @abstractmethod
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
            
    



