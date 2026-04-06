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
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    
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

# class Pessoa():
#     def __init__(self, nome, idade):
#         self._nome = nome
#         self._idade = idade

#     @property
#     def nome(self):
#         return self._nome

#     @property
#     def idade(self):
#         return self._idade
    
# from abc import ABC, abstractmethod

# class Conta(ABC):
#     def __init__(self, agencia, numero_conta, saldo):
#         self.agencia = agencia
#         self.numero_conta = numero_conta
#         self.saldo = saldo

#     def depositar(self, valor):
#         self.saldo += valor

#     @abstractmethod
#     def sacar(self, valor):
#         ...

# class ContaCorrente(Conta):
#     def __init__(self, agencia, numero_conta, saldo, limite):
#         super().__init__(agencia, numero_conta, saldo)
#         self.limite = limite

#     def sacar(self, valor):
#         ...
            
# class ContaPoupanca(Conta):
#     ...
            
# class Banco:
#     def __init__(self):
#         self.clientes = []
#         self.contas = []
#         self.agencias = []

#     def autenticar(self, cliente):
#         return (
#             cliente in self.clientes and
#             cliente.conta in self.contas and
#             cliente.conta.agencia in self.agencias
#         )


# class Cliente(Pessoa):
#     def __init__(self, nome, idade):
#         super().__init__(nome, idade)
#         self.conta = None
    
#     def conta(self):
#         for conta in self._contas:
#             print(conta.nome)
#         print()
        

    
# class ContaCorrente(Conta):
#     def __init__(self):
#         if self.conta == "Conta corrente":
#             print('Recebeu R$1.000,00 de limite')

        
# class ContaPoupanca(Conta):
#     ...
        
        
        
########## Correção

