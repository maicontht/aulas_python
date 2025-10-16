"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança) X
    Pessoa tem nome e idade (com getters) x
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta X
    ContaCorrente deve ter um limite extra X
    Contas têm agência, número da conta e saldo x
    Contas devem ter método para depósito 
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

# MY Resolution

from abc import ABC, abstractmethod

class Banco:
    def __init__(self, banco):
        self.banco = banco
        self.clientes = []
        self.contas = []

class Conta(ABC):
    def __init__(self,agencia):
        self.agencia = agencia
        self.conta = None
        self.saldo = None
        self.deposito = None

    @abstractmethod
    def depositar(self, valor):
        pass


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.limite_saque = 1000
        self.deposito = None

    def depositar(self, valor):
        pass
    
    

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.limite_saque = 1500
        self.deposito = None

    def depositar(self, valor):
        pass    
        

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_idade(self):
        return self.idade
    
    def set_idade(self, t_idade):
        if t_idade > 18 and t_idade < 100:
            self.idade = t_idade
        else: 
            print('idade invalida')        

class Cliente(Pessoa):
    ...

p1 = Cliente('João', 30)
bradesco = Banco('Bradesco')
conta1 = ContaCorrente(1234, 56789-0, 1000)
print(conta1.saldo)