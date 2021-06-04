#Aluno: Thomas Alberto de Castro Neto
#Atividade: Exercício Laboratório 2
#Professora: Karla Donato
#Disciplina: CES22


from abc import ABC, abstractmethod
from typing import Optional

class Order(ABC): #Command
    
    @abstractmethod
    def execute(self):
        pass
    
    
class VerExtrato(Order): #ConcreteCommand
    
    def __init__(self, aplicacao):
        self.aplicacao = aplicacao
        
    def execute(self):
        self.aplicacao.extrato()
        
        
class VerSaldo(Order): #ConcreteCommand
    
    def __init__(self, aplicacao):
        self.aplicacao = aplicacao
        
    def execute(self):
        self.aplicacao.saldo()
        
        
class Transferir(Order): #ConcreteCommand
    def __init__(self, aplicacao):
        self.aplicacao = aplicacao
        
    def execute(self):
        self.aplicacao.transferir()
        
class Aplicacao: #Receiver
    
    def extrato(self):        
        print('Você verá seu extrato.')
        
    def saldo(self):
        print('Você verá seu saldo.')
        
    def transferir(self):
        print('Você fará uma transferência')
        
        
class Banco: #Invoker
    
    def __init__(self):
        self.__order_queue = []
        
    def place_order(self, order):
        self.order = order
        order.execute()
        
        
        
#Cliente
aplicacao = Aplicacao()
extrato = VerExtrato(aplicacao)
saldo = VerSaldo(aplicacao)
transferencia = Transferir(aplicacao)

#Banco
banco = Banco()
banco.place_order(extrato)
banco.place_order(saldo)
banco.place_order(transferencia)